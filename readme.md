****************************************** BACK END *********************************************************************
El paso principal es ubicarnos en el directorio de la app por medio de la linea de comandos, ya sea para ejecutarse de forma directa o utilizando docker

EJECUCION DIRECTA
Generamos ambiente virtual de python con el siguiente comando
python3 -m venv rac

Ejecutamos el workspace rac con el siguiente comando
rac/scripts/activate

Instalamos la version ultima de flask
pip install flask

Generamos el archivo de requirements con el siguiente comando
pip freeze > requirements.txt

Ejecutamos el archivo de requirement.txt para instalar las dependencias
pip install -r requirements.txt

Actualizamos la libreria para instalacion de paquetes pip
python -m pip install --upgrade pip

Para ejecutar la app en local se puede ejecutar el siguiente comando
python3 app.py

EJECUCION POR DOCKER
En el caso de usar Docker, se ejecuta el siguiente comando
docker compose -f docker-compose.yml up --build  -d

****************************************** FRONT END *********************************************************************

Para ejecutarse localmente despues de haber levantado el Back end con python, se deben ejecutar la siguiente secuencia de comandos

Clonar desde el repositorio con el comando siguiente
git clone del repo

Contar con la version 16 de angular minimo, node y despues ejecutar el siguiente comando para isntalar las dependencias
npm i

Ejecutar la app en local
ng serve

Abrir el navegador colocando la siguiente URL en la barra de navegacion del navegador
http://localhost:4200