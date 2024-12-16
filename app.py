import streamlit as st
import psycopg2
import csv
import io
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completed = Column(Boolean, default=False)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def add_task(title, description, completed=False):
    new_task = Task(title=title, description=description, completed=completed)
    session.add(new_task)
    session.commit()

def list_tasks():
    return session.query(Task).all()

def mark_task_completed(task_id):
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = True
        session.commit()

def delete_completed_task(task_id):
    task = session.query(Task).filter(Task.id == task_id, Task.completed == True).first()
    if task:
        session.delete(task)
        session.commit()

def export_tasks_to_csv():
    tasks = session.query(Task).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Título', 'Descripción', 'Completada'])
    for task in tasks:
        writer.writerow([task.id, task.title, task.description, task.completed])
    return output.getvalue()

def import_tasks_from_csv(file):
    try:
        df = pd.read_csv(file)
        for _, row in df.iterrows():
            add_task(
                title=row['Título'],
                description=row['Descripción'],
                completed=row['Completada']
            )
        return True
    except Exception as e:
        st.error(f"Error al importar: {e}")
        return False

def render_task_list():
    tasks = list_tasks()
    for task in tasks:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"{task.title} - {'Completada' if task.completed else 'Pendiente'}")
        
        with col2:
            action_key = "action_{}".format(task.id)
            if not task.completed:
                if st.button("Completar", key="complete_{}".format(action_key)):
                    mark_task_completed(task.id)
                    st.success("Tarea '{}' marcada como completada".format(task.title))
                    st.rerun()
            else:
                if st.button("Eliminar", key="delete_{}".format(action_key)):
                    delete_completed_task(task.id)
                    st.success("Tarea '{}' eliminada".format(task.title))
                    st.rerun()

def render_task_input_form():
    with st.form(key='add_task_form'):
        title = st.text_input("Título de la tarea")
        description = st.text_area("Descripción de la tarea")
        submit_button = st.form_submit_button("Agregar Tarea")
       
        if submit_button:
            if title.strip():
                add_task(title, description)
                st.success("Tarea agregada exitosamente!")
                st.rerun()
            else:
                st.warning("El título de la tarea es obligatorio")

def render_task_import_tab():
    uploaded_file = st.file_uploader("Selecciona un archivo CSV", type="csv")
    if uploaded_file is not None and st.button("Importar Tareas"):
        if import_tasks_from_csv(uploaded_file):
            st.success("Tareas importadas exitosamente!")
            st.rerun()

def render_task_export_tab():
    if st.button("Descargar Tareas en CSV"):
        csv_content = export_tasks_to_csv()
        st.download_button(
            label="Descargar CSV",
            data=csv_content,
            file_name="tareas.csv",
            mime="text/csv"
        )
        st.rerun()

def main():
    st.title("Gestión de Tareas")
    
    tab1, tab2, tab3 = st.tabs(["Tareas", "Importar", "Exportar"])
    
    with tab1:
        render_task_input_form()
        render_task_list()
    
    with tab2:
        st.header("Importar Tareas")
        render_task_import_tab()
    
    with tab3:
        st.header("Exportar Tareas")
        render_task_export_tab()

if __name__ == "__main__":
    main()