# 💻 Primera API con Django Rest Framework  
Una aplicación web desarrollada con Django Rest Framework, estructurada de manera clara para construir y exponer APIs RESTful de forma eficiente.

## 📃 Descripción General

Este proyecto sigue una estructura personalizada:
- `src/`: Directorio principal del código  
  - `config/`: Configuración del proyecto  
  - `series/`: Aplicación principal de Series  
- `venv/`: Entorno virtual (no incluido en Git)

## 🔍 Requisitos Previos

- Python >= 3.12  
- Editor de texto (Visual Studio Code, PyCharm, etc.)

## 🔧 Instalación

Sigue estos pasos para crear y ejecutar el proyecto:

1. **Clona este repositorio**

2. **Crea y activa el entorno virtual**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3.  **Instala las dependencias**

    ```bash
    cd src
    pip install -r requirements.txt
    ```

4.  **Aplica Migraciones**

    ```bash
    python manage.py migrate
    ```
    
## 🚀 Corre el proyecto
```bash
    cd src
    python manage.py runserver
```

Accede al sitio usando `http://127.0.0.1:8000/series/api/v1/`

## 🛠 Configuración
- Agrega modelos en series/models.py
- Crea serializers en series/serializers.py
- Define las vistas en series/views.py
- Configura las rutas en series/urls.py

## 👤 Autores
Baltazar Llique Franklin Anderson
Garcia Castillejo Rafael
Rodriguez Ordoñez Juan Daniel



 
