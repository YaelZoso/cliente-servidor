from flask import Flask, request, jsonify
from servicios import juego_vida


app = Flask(__name__)


@app.route('/mensaje')
def enviar_mensaje():
    return "Hola mundo desde el servidor"

@app.route("/vida", methods=["GET", "POST"])
def procesar_vida():
    if request.method == "POST":
        datos = request.get_json()
        tablero = datos.get("tablero")
        if tablero:
            nueva_gen = juego_vida.siguiente_generacion(tablero)
            return jsonify({"tablero": nueva_gen})
        else:
            return jsonify({"error": "No se proporcionó el tablero"}), 400
    else:
        return """
        <h2>Servidor del Juego de la Vida</h2>
        <p>Usa esta ruta para enviar un tablero con una petición POST.</p>
        <p>Ejemplo de uso: cliente.py o interfaz.py</p>
        """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    