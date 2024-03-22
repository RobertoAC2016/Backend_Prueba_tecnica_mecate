from flask import Flask, jsonify
from flasgger import Swagger
import requests as req
from flask_cors import CORS
from MySqlConnection import MySQLConnection

app = Flask(__name__)
CORS(app)
Swagger(app)

@app.route('/', methods=['GET'])
def index():
    """
    Endpoint de inicio home

    Este es un Endpoint de cómo se puede usar Flask y Flasgger para definir endpoints con documentación Swagger.
    Author: RAC
    Contact: keepteacher@gmail.com
    Version: 1.0

    responses:
      200:
        description: Mensaje de saludo
    """
    return '¡Hola, mundo! Esta es una API-REST V1.'

@app.route('/data', methods=['GET'])
def get_data():
    """
    Endpoint para obtener los datos de un API de terceros

    Este es un Endpoint para regresar los datos del API en formato json.
    Author: RAC
    Contact: keepteacher@gmail.com
    Version: 1.0

    ---
    parameters:
      - params: Los parametros vienen en la URL
        description: No se necesita ningun parametro adicional
    responses:
      200:
        status: Booleano
        data: datos del api
        message: mensaje de error o exito en la peticion
    """
    url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
    response = req.get(url)
    data = None
    msg = None
    status = True
    if response.status_code == 200:
        data = response.json()
        msg = "success"
    else:
        print('Error en la solicitud. Código de estado:', response.status_code)
        msg = f'Rason: {response.reason}, status_code: {response.status_code}'
        status = False
    return jsonify({'status': status, 'message': msg, 'data': data})

@app.route('/vuelos', methods=['GET'])
def get_stats():
    """
    Endpoint para obtener los datos de las estadisticas de vuelos

    Este es un Endpoint para regresar los datos de los vuelos API en formato json, que responden a las siguientes 4 preguntas:
    1. Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año?
    2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año?
    3. ¿En qué día se han tenido mayor número de vuelos?
    4. ¿Cuáles son las aerolineas que tienen mas de 2 vuelos por día?
    Author: RAC
    Contact: keepteacher@gmail.com
    Version: 1.0
    Description: Este EP no requiere parametros en el body ya que es de tipo GET y solo es de consulta
    ---
    responses:
      200:
        status: Booleano
        data: JSON
        message: mensaje de error o exito en la peticion
    """
    data = {
      "aeropuerto_max_vuelos":0,
      "aerolinea_max_vuelos":0,
      "dia_max_vuelos":0,
      "aerolinea_max_por_dia":[]
    }
    try:
      results = None
      with MySQLConnection() as cnx:
          with cnx.newCommand() as command:
              command.Command = """
              select (select nombre from aeropuertos where id = id_aeropuerto) as name, count(id_aeropuerto) as mayor from vuelos group by id_aeropuerto order by 2 desc limit 1;
              """
              results = command.execute().fetchall()
              if results:
                    for row in list(results):
                      data["aeropuerto_max_vuelos"] = row["name"]
              command.Command = """
              select (select nombre from aerolineas where id = id_aerolinea) as name, count(id_aerolinea) as mayor from vuelos group by id_aerolinea order by 2 desc limit 1;
              """
              results = command.execute().fetchall()
              if results:
                  for row in list(results):
                        data["aerolinea_max_vuelos"] = row["name"]
              command.Command = """
              select dia as name, count(dia) from vuelos group by dia order by 2 desc limit 1;
              """
              results = command.execute().fetchall()
              if results:
                  for row in list(results):
                      data["dia_max_vuelos"] = row["name"]
              command.Command = """
              select (select nombre from aerolineas where id = id_aerolinea) as name, count(dia) as mayor from vuelos group by id_aerolinea having count(dia) > 2 order by 2 desc;
              """
              results = command.execute().fetchall()
              if results:
                  for row in list(results):
                      data["aerolinea_max_por_dia"].append(row["name"])
      
      msg = "success"
      status = True
    except Exception as e:
      msg = f"Error:{str(e)}"
      status = False
    return jsonify({'status': status, 'message': msg, 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
