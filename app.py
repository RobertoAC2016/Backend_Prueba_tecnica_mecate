from flask import Flask, jsonify
from flasgger import Swagger
import requests as req
from flask_cors import CORS

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
