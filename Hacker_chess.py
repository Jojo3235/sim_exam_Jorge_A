#Hackerchess

import math as m
import os
import random as rd
import re
import sys

# Define the board

def verticalRooks(r1, r2):



board = np.array([['R','N','B','Q','K','B','N','R'],
                    ['P','P','P','P','P','P','P','P'],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                    ['p','p','p','p','p','p','p','p'],
                    ['r','n','b','q','k','b','n','r']])
print(board)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
    r1 = []
    for _ in range(n):
        r1_item = int(input().strip())
        r1.append(r1_item)
        r2 = []
    for _ in range(n):
        r2_item = int(input().strip())
        r2.append(r2_item)
        result = verticalRooks(r1, r2)
        fptr.write(result + '\n')
        fptr.close()