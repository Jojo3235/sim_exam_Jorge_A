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
def verticalRooksPos(r1, r2):
    r1 = np.where(board == r1)
    r2 = np.where(board == r2)
    h1 = r1[0]
    h2 = r2[0]
    return h1[0], h2[0]



if __name__ == '__main__':
    print(verticalRooksPos('R1', 'r1'))