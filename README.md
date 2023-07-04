# Apuntes para iniciar app en Django

- Primeramente installar django con pipenv o pip install django
- Luego "django-admin startproject 'nombre_projecto' ." inicia el projecto
- Comando "python manage.py runserver" inicia el projecto
- Comando "python manage.py startapp 'nombre_app'" crea una app dentro del projecto
- Para hacer migraciones, usar comando "python manage.py makemigrations" luego "python manage.py migrate"
- Para crear usuarios admin "python manage.py createsuperuser"