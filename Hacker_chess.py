#Hackerchess

import numpy as np

board = np.array([['R','N','B','Q','K','B','N','R'],
                    ['P','P','P','P','P','P','P','P'],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    ['p','p','p','p','p','p','p','p'],
                    ['r','n','b','q','k','b','n','r']])

#Para R y r
def verticalRooks(r1, r2):
    r1 = np.where(board == r1)
    r2 = np.where(board == r2)
    return r1, r2

if __name__ == '__main__':
    print(verticalRooks('R', 'r'))