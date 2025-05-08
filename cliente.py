import requests

tablero = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

url = 'http://127.0.0.1:5000/vida'

respuesta = requests.post(url, json={"tablero": tablero})

if respuesta.status_code == 200:
    nuevo = respuesta.json()["tablero"]
    print("siguiente generacion:")
    for fila in nuevo:
        print(fila)
    else:
        print("error:", respuesta.status_code, respuesta.text)
