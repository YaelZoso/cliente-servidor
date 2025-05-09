import requests
import tkinter as tk


class ClienteVida:
    def __init__(self, master):
        self.url = 'http://127.0.0.1:5000/vida'
        self.master = master
        self.tamano_celda = 20  # Tamaño de cada celda en píxeles
        self.intervalo = 200  # Intervalo en milisegundos

        self.peticion()
        self.filas = len(self.tablero)
        self.columnas = len(self.tablero[0])
        self.canvas = tk.Canvas(master, width=self.columnas *
                                self.tamano_celda,
                                height=self.filas *
                                self.tamano_celda, bg="white")
        self.canvas.pack()
        self.actualizar()

    def peticion(self):

        respuesta = requests.get(self.url)

        if respuesta.status_code == 200:
            self.tablero = respuesta.json()["tablero"]

    def dibujar_tablero(self):
        self.canvas.delete("all")
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j]:
                    x1 = j * self.tamano_celda
                    y1 = i * self.tamano_celda
                    x2 = x1 + self.tamano_celda
                    y2 = y1 + self.tamano_celda
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    def actualizar(self):
        self.dibujar_tablero()
        self.peticion()
        self.master.after(self.intervalo, self.actualizar)


# Crear ventana
ventana = tk.Tk()
ventana.title("Juego de la Vida")
juego = ClienteVida(ventana)
ventana.mainloop()
