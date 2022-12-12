import numpy as np

piezas = {'R': '\u265C',
            'r': '\u2656',
}

R = piezas['R']
r = piezas['r']

def pedir_numero():
    n = int(input('Introduce el tamaño del tablero: '))
    return n


def crear_tablero(n):
    tablero = np.empty((n,n), dtype=str)
    for i in range(n):
        for j in range(n):
            tablero[i][j]=' '
    return tablero


def colocar_torre():
    n = pedir_numero()
    tablero = crear_tablero(n)
    if 0<n-1:
        for i in range(n):
            tablero[0][i]=r
            tablero[n-1][i]=R
    else:
        pass
    return tablero

print(colocar_torre())