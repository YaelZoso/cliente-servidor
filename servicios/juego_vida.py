import random


def contar_vecinas_vivas(tablero, x, y):
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinas = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),          (0, 1),
               (1, -1),  (1, 0), (1, 1)]
    vivas = 0
    for dx, dy in vecinas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < filas and 0 <= ny < columnas: 
            vivas += tablero[nx][ny]
    return vivas


def siguiente_generacion(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            vivas = contar_vecinas_vivas(tablero, i, j)
            if tablero[i][j] == 1 and vivas in [2, 3]:
                nuevo_tablero[i][j] = 1
            elif tablero[i][j] == 0 and vivas == 3:
                nuevo_tablero[i][j] = 1
    return nuevo_tablero
