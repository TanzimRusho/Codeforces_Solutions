import numpy as np
import math
from collections import deque

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    #print (matrix)
    return int(matrix[size_x - 1, size_y - 1])
    
    
#print(levenshtein("1073741824", "1000000000"))    
    

t = int(input())

powers = deque()

for i in range(40):
    powers.append(str(2**i))
    
#print(powers)


for i in range(t):
    number = input()
    
    #length = len(number)

    dif = deque()

    for power in powers:
        dif.append(levenshtein(number, power))
      
    print(dif)    
    print(min(dif))
        




    
    

    
    