import numpy as np
#crear array de 8x8
def crear_tablero():
    tablero = np.empty((8,8), dtype=str)
    for i in range(8):
        for j in range(8):
            tablero[i][j]=' '
    tablero[1][0]=34
    return tablero

tablero = crear_tablero()

print(tablero)
print(tablero[:,0])