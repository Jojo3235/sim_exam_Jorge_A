import numpy as np

piezas = {'R': '\u265C',
            'r': '\u2656',
}

R = piezas['R']
r = piezas['r']

def pedir_numero(cond):
    n = int(input('Introduce un número para {}: '.format(cond)))
    return n


def crear_tablero(n):
    tablero = np.empty((n,n), dtype=str)
    for i in range(n):
        for j in range(n):
            tablero[i][j]=' '
    return tablero


def colocar_torre():
    n = pedir_numero("definir el tamaño del tablero")
    tablero = crear_tablero(n)
    if 0<n-1:
        for i in range(n):
            tablero[0][i]=r
            tablero[1][i]=R
    else:
        pass
    tablero[0][0]=R
    tablero[1][0]=' '
    tablero[n-1][0]=r
    return tablero

#detectar la posicion de una unica torre blanca
def seleccionar_torre_blanca(tablero):
    posicion = []
    n = pedir_numero("seleccionar la torre blanca")
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == R:
                posicion.append([i,j])
    posicion_n = posicion[n-1]
    return posicion_n


def seleccionar_torre_negra(tablero):
    posicion = []
    n = pedir_numero("seleccionar la torre negra")
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == r:
                posicion.append([i,j])
    posicion_n = posicion[n-1]
    return posicion_n


#movimiento de las torres   
def movimiento_torre():
    tablero = colocar_torre()
    seleccionar_torre_blanca(tablero)
    numero_casillas = pedir_numero("mover la torre")
    s = str(r)
    r = tablero[s-1][2]
    h = r[0]
    v = r[1]
    pos = [h[0], v[0]]
    if pos[0] + numero_casillas < 8:
        tablero[pos[0] + numero_casillas][pos[1]] = s
        tablero[pos[0]][pos[1]] = ' '
    else:
        print('Movimiento no válido')
    return tablero

print(seleccionar_torre_negra(colocar_torre()))