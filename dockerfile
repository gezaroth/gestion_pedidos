# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN apt-get update && \
    apt-get install -y pkg-config libmariadb-dev-compat build-essential
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente al directorio de trabajo
COPY . .

# Exponer el puerto 8000 para que pueda ser accesible desde fuera del contenedor
EXPOSE 8000

# Comando para ejecutar el servidor Django cuando se inicie el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
