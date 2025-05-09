from flask import Flask, request, jsonify
from servicios import juego_vida


app = Flask(__name__)

tablero = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]


@app.route('/mensaje')
def enviar_mensaje():
    return "Hola mundo desde el servidor"


@app.route("/vida")
def procesar_vida():
    global tablero
    if tablero:
        nueva_gen = juego_vida.siguiente_generacion(tablero)
        tablero = nueva_gen
        return jsonify({"tablero": nueva_gen})
    else:
        return jsonify({"error": "No se proporcionó el tablero"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
