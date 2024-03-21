# Usa la imagen base de Python version 3.9
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Actualizamos la libreria de instalacion de paquetes
RUN python -m pip install --upgrade pip

# Copia el código de la aplicación al contenedor
COPY . .

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]

