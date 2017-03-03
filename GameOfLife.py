############################################################
#part1
def createOneRow(width):
    row=[]
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    A=[]
    for row in range(height):
        A += [createOneRow(width)]
    return A
############################################################
#part2
import sys
def printBoard(A):
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')
############################################################
#part3
def diagonalize(width, height):
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
############################################################
#part4
def innerCells(w, h):
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
                A[row][col]=1
    return A
############################################################
#part5
import random
def randomCells(w, h):
    A = createBoard(w, h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            A[row][col] = random.choice([0,1])
    return A
############################################################
#part6
from copy import deepcopy
def copy(A):
    newA = deepcopy(oldA)
    return newA
############################################################
#part7
def innerReverse(A):
    for row in range(1, len(A)-1):
        for col in range(1, len(A[0])-1):
            if A[row][col]==0:
                A[row][col]=1
            else:
                A[row][col]=0
    return A
############################################################
    

