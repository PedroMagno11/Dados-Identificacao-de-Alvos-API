from flask import Flask, jsonify
from preconfigured_data import preconfidured_data
from random import randint
from flask_cors import CORS

app = Flask(__name__)

# habilita CORS para todas requisições do tipo GET 
# para todas as origens
CORS(app=app, resources={r"/*":{"origins": "*", "methods":["GET"]}})

@app.route('/target', methods=['GET'])
def get_target():

    indice_navio_sorteado = randint(0, preconfidured_data.__len__() - 1)
    navio_sorteado = preconfidured_data[indice_navio_sorteado]
    return jsonify(navio_sorteado)

if __name__== '__main__':
    app.run()