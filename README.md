﻿# 💻 First API in Django Rest Framework
A web application developed with Django Rest Framework, clearly structured to efficiently build and expose RESTful APIs.

## 📃 Overview

This project follows a custom structure:
- `src/`: Main code directory
  - `config/`: Project configuration
  - `quizzes/`: Main application
  - `categories/`: Second application
- `venv/`: Virtual environment (not tracked in git)

## 🔍 Prior Requirements

-   Python >= 3.12
-   Any text editor

## 🔧 Instalation

Follow these steps to create a project using Django:

1.  **Clone this repository**

2.  **Create and activate virtual environment**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
    > If `.\venv\Scripts\activate` use this code first `Set-ExecutionPolicy Unrestricted -Scope Process`. This allows the use of scripts in the system.

3.  **Install dependencies**

    ```bash
    cd src
    pip install -r requirements.txt
    ```

4.  **Apply migrations**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser**

    ```bash
    python manage.py createsuperuser
    ```
    
## 🚀 Running the project
```bash
    cd src
    python manage.py runserver
```

Access the site at `http://127.0.0.1:8000/api/` for Quizzes, `http://127.0.0.1:8000/api/description/` for Categories and admin at `http://127.0.0.1:8000/admin/`

## 🛠 Development
- Add models to quizzes/models.py
- Create serializers in quizzes/serializers.py
- Create views in quizzes/views.py
- Add URL patterns in quizzes/urls.py

## 👤 Autors
Baltazar Llique Franklin Anderson
Garcia Castillejo Rafael
Rodriguez Ordoñez Juan Daniel

  
##
Built with ❤️ using Django 5 and Django Rest Frameworks



 
