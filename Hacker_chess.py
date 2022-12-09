#Hackerchess

import numpy as np

board = np.array([['R1','N','B','Q','K','B','N','R2'],
                    ['P','P','P','P','P','P','P','P'],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    ['p','p','p','p','p','p','p','p'],
                    ['r1','n','b','q','k','b','n','r2']])

#Para R y r
def RooksPosnogener(r1, r2):
    r1 = np.where(board == r1)
    r2 = np.where(board == r2)
    h1 = r1[0]
    h2 = r2[0]
    v1 = r1[1]
    v2 = r2[1]
    posr1 = [h1[0], v1[0]]
    posr2 = [h2[0], v2[0]]
    return posr1, posr2

#Rookspos for *args
def RooksPos(*args):
    for i in args:
        i = np.where(board == i)
        h = i[0]
        v = i[1]
        pos = [h[0], v[0]]
        return pos


#definir el movimiento de la torre 
def rookMove(r1, numero_casillas):
    np.where(board == r1+numero_casillas)

if __name__ == '__main__':
    print(RooksPos('R1', 'r1'))