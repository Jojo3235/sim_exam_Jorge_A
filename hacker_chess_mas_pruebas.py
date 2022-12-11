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

#print(colocar_torre())
def seleccionar_torre(tablero):
    n = pedir_numero("seleccionar la torre")
    
#movimiento de las torres   
def movimiento_torre(s):
    tablero = colocar_torre()
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

print(movimiento_torre())