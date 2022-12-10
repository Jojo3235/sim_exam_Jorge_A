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


def RooksPos(*args):
    for i in args:
        i = np.where(board == i)
        h = i[0]
        v = i[1]
        pos = [h[0], v[0]]
        return pos

def rpos(*args):
    list = []
    for i in args:
        posr = RooksPos(i)
        list.append(posr)
    return list

def rookMove(r1, numero_casillas):
    s = str(r1)
    r1 = np.where(board == r1)
    h = r1[0]
    v = r1[1]
    pos = [h[0], v[0]]
    if pos[0] + numero_casillas < 8:
        board[pos[0] + numero_casillas][pos[1]] = s
        board[pos[0]][pos[1]] = ' '
    else:
        print('Movimiento no válido')
    return board

if __name__ == '__main__':
    print(rpos('R1', 'R2', 'r1', 'r2'))
    print(rookMove('Q', 3))