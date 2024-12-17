# PythonTaskApp

Este proyecto es una aplicación de gestión de tareas desarrollada en **Python** utilizando **SQLAlchemy** como ORM y **PostgreSQL** como base de datos. Permite importar y exportar tareas a través de archivos **CSV**, facilitando la gestión y administración de tus tareas.

---

## Requisitos previos

Asegúrate de tener instalados los siguientes componentes:

1. **Python 3.8+** (recomendado)
2. **PostgreSQL** configurado localmente o a través de un servicio web (Railway, Render, ElephantSQL, etc.).
3. Librerías de Python necesarias para el proyecto.

Puedes instalar las dependencias usando el archivo **requirements.txt**:

```bash
pip install -r requirements.txt
```

---

## Estructura del proyecto

El proyecto sigue esta estructura:

```plaintext
project-root/
|-- app.py                 # Archivo principal del proyecto
|-- .env                   # Variables de entorno (configuración de la DB)
|-- requirements.txt       # Lista de dependencias del proyecto
```

---

## Inicialización del proyecto

Sigue estos pasos para inicializar la aplicación:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/DaroOps/PythonTaskApp.git
   cd PythonTaskApp
   ```

2. **Crear un entorno virtual** (opcional, recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno**:
   Crea el archivo `.env` siguiendo el ejemplo proporcionado:

   ```plaintext
   DATABASE_URL=postgresql://<USER>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>
   ```

5. **Ejecutar la aplicación**:
   ```bash
   streamlit run app.py
   ```

---


## Funciones principales

- **Importar tareas** desde un archivo CSV.
- **Exportar tareas** a un archivo CSV.
- **Persistencia de tareas** en una base de datos PostgreSQL.

---

## Requerimientos adicionales

Las dependencias requeridas para el proyecto están en **requirements.txt**:

```plaintext
altair==5.5.0
attrs==24.2.0
blinker==1.9.0
cachetools==5.5.0
certifi==2024.12.14
charset-normalizer==3.4.0
click==8.1.7
colorama==0.4.6
gitdb==4.0.11
GitPython==3.1.43
greenlet==3.1.1
idna==3.10
Jinja2==3.1.4
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
narwhals==1.18.4
numpy==2.2.0
packaging==24.2
pandas==2.2.3
pillow==11.0.0
protobuf==5.29.1
psycopg2==2.9.10
psycopg2-binary==2.9.10
pyarrow==18.1.0
pydeck==0.9.1
Pygments==2.18.0
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.2
referencing==0.35.1
requests==2.32.3
rich==13.9.4
rpds-py==0.22.3
six==1.17.0
smmap==5.0.1
SQLAlchemy==2.0.36
streamlit==1.41.1
tenacity==9.0.0
toml==0.10.2
tornado==6.4.2
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
watchdog==6.0.0
```

Si necesitas reinstalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## Notas

1. Si usas Railway, Render u otro servicio web, asegúrate de configurar las variables de entorno correspondientes.
2. Si PostgreSQL está en una instancia local, verifica que el puerto 5432 esté abierto.
3. Para formato de fecha, se está utilizando **`%Y-%m-%d %H:%M:%S`** (UTC).

---

## Contribuciones

Las contribuciones son bienvenidas. Para reportar errores o sugerir mejoras, abre un **issue** en este repositorio.

---

### Autor

**[DaroOps]**  
Desarrollador Full Stack
