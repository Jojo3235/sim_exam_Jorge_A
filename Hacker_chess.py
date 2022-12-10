#Hackerchess

import numpy as np
import unittest

piezas = {'P1': '\u2659',
            'P2': '\u2659',
            'P3': '\u2659',
            'P4': '\u2659',
            'P5': '\u2659',
            'P6': '\u2659',
            'P7': '\u2659',
            'P8': '\u2659',
            'p1': '\u265F',
            'p2': '\u265F',
            'p3': '\u265F',
            'p4': '\u265F',
            'p5': '\u265F',
            'p6': '\u265F',
            'p7': '\u265F',
            'p8': '\u265F',
            'R1': '\u2656',
            'R2': '\u2656',
            'r1': '\u265C',
            'r2': '\u265C', 
            'N1': '\u2658',
            'N2': '\u2658', 
            'n1': '\u265E',
            'n2': '\u265E', 
            'B1': '\u2657',
            'B2': '\u2657', 
            'b1': '\u265D',
            'b2': '\u265D', 
            'Q': '\u2655', 
            'q': '\u265B', 
            'K': '\u2654', 
            'k': '\u265A'
            }

#asignar cada pieza a su valor dentro del diccionario
P1 = piezas['P1']
P2 = piezas['P2']
P3 = piezas['P3']
P4 = piezas['P4']
P5 = piezas['P5']
P6 = piezas['P6']
P7 = piezas['P7']
P8 = piezas['P8']
p1 = piezas['p1']
p2 = piezas['p2']
p3 = piezas['p3']
p4 = piezas['p4']
p5 = piezas['p5']
p6 = piezas['p6']
p7 = piezas['p7']
p8 = piezas['p8']
R1 = piezas['R1']
R2 = piezas['R2']
r1 = piezas['r1']
r2 = piezas['r2']
N1 = piezas['N1']
N2 = piezas['N2']
n1 = piezas['n1']
n2 = piezas['n2']
B1 = piezas['B1']
B2 = piezas['B2']
b1 = piezas['b1']
b2 = piezas['b2']
Q = piezas['Q']
q = piezas['q']
K = piezas['K']
k = piezas['k']


board = np.array([[R1,N1,B1,Q,K,B2,N2,R2],
                    [P1,P2,P3,P4,P5,P6,P7,P8],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [p8,p7,p6,p5,p4,p3,p2,p1],
                    [r2,n2,b2,q,k,b1,n1,r1]])


def Pos(*args):
    for i in args:
        i = np.where(board == i)
        h = i[0]
        v = i[1]
        pos = [h[0], v[0]]
        return pos

def pos(*args):
    list = []
    for i in args:
        posr = Pos(i)
        list.append(posr)
    return list

def Move(r1, numero_casillas):
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

def detectar_piezas_blancas(*args):
    listwhite = []
    if args == args.capitalize():
        listwhite.append(args)
    else:
        pass
    return listwhite

def detectar_piezas_negras(*args):
    listblack = []
    if args == args.lower():
        listblack.append(args)
    else:
        pass
    return listblack

if __name__ == '__main__':
    print(pos(R1, R2, r1, r2))
    print(Move(Q, 3))
    unittest.main()