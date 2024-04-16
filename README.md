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







### Extra - Contenedor Docker:

Si deseas desplegar la aplicación en un contenedor, como Docker, sigue estas indicaciones:

1. **Obtener la imagen de MySQL**: Si no tienes la imagen de MySQL, ejecuta en la terminal:
   ```bash
   docker pull mysql


Iniciar el contenedor de MySQL: Ejecuta el siguiente comando para crear y ejecutar un contenedor MySQL:
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=PSSWRD -d mysql


Construir la imagen del proyecto: Ve a la ruta del proyecto (donde se encuentra el Dockerfile y el requirements.txt) y ejecuta:
docker build -t gestion-pedidos .


Obtener la dirección IP del contenedor de la base de datos: Para obtener la dirección IP, ejecuta en la terminal:
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql-container


Modificar la configuración en settings.py: Actualiza la configuración de la base de datos en settings.py con la dirección IP obtenida:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pedidos',
        'USER': 'root',
        'PASSWORD':'MYSQLPASSWRD',
        'HOST': '172.17.0.2',
        'PORT':'3306'
    }
}


Crear la base de datos: Inicia sesión en el contenedor de MySQL y crea la base de datos ejecutando los siguientes comandos:
docker exec -it mysql-container bash
bash-4.4# mysql -u root -p


Una vez dentro de MySQL, ejecuta:
CREATE DATABASE pedidos;
exit;
Luego, sal del contenedor MySQL:
exit


Migrar las tablas y datos a la base de datos: Ejecuta en la terminal:
docker exec -it <ID DE LA IMAGEN DEL API> python manage.py migrate


Crear un superusuario: Para gestionar desde el panel de Django, ejecuta:
docker exec -it <ID DE LA IMAGEN DEL API> python manage.py createsuperuser


Ejecutar la imagen de la API desarrollada en Django: Finalmente, ejecuta:
docker run -p 8000:8000 gestion-pedidos


Espero que esta versión sea útil para ti. Si necesitas más ayuda, ¡no dudes en preguntar!
