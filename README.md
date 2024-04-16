# Aplicación de Gestión de Pedidos

Esta es una aplicación de gestión de pedidos desarrollada con Django y Django REST Framework.

## Requisitos

- Python 3.x
- Django
- Django REST Framework
- MySQL

## Instalación

1. Clona este repositorio en tu máquina local:


```bash
git clone https://github.com/tu_usuario/gestion_pedidos.git


Instala las dependencias del proyecto:
cd nombre_del_repositorio
pip install -r requirements.txt


Configura la base de datos en el archivo settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_de_la_base_de_datos',
        'USER': 'usuario_de_la_base_de_datos',
        'PASSWORD': 'contraseña_de_la_base_de_datos',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

conecta el file mydb.py con los datos de tu bdd en este caso mysql



Realiza las migraciones de la base de datos:

python manage.py makemigrations
python manage.py migrate


python manage.py runserver
'http://127.0.0.1:8000/admin'


 Uso
Puedes acceder al panel de administración de Django para gestionar los artículos y pedidos en http://127.0.0.1:8000/admin/.

Para interactuar con la API REST, puedes utilizar herramientas como Postman o realizar peticiones HTTP desde tu código.


Contribuir
Si deseas contribuir a este proyecto, ¡estamos abiertos a colaboraciones! Siéntete libre de bifurcar este repositorio y enviar solicitudes de extracción con tus mejoras.


Este README proporciona una visión general de cómo instalar, configurar y utilizar la aplicación de gestión de pedidos, así como cómo contribuir al proyecto. Puedes personalizarlo según las necesidades específicas de tu proyecto.
