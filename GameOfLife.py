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
#part8
def countNeighbors(row, col, A):
    '''This function determines the number of alive neighbors
       around the cell in a particular location.'''
    liveCounter = 0
    #if statements below this comment check for neighbors
    #diagonal to the cell.
    if A[row-1][col-1] == 1:
        liveCounter += 1
    if A[row+1][col+1] == 1:
        liveCounter += 1
    if A[row-1][col+1] == 1:
        liveCounter += 1
    if A[row+1][col-1] == 1:
        liveCounter += 1
    #if statements below this comment check for neighbors
    #above, below, left and right to the cell. 
    if A[row-1][col] == 1:
        liveCounter += 1
    if A[row+1][col] == 1:
        liveCounter += 1
    if A[row][col-1] == 1:
        liveCounter += 1
    if A[row][col+1] == 1:
        liveCounter += 1
    return liveCounter
############################################################
#part9
def next_life_generation(A):
    '''makes a copy of A and then advanced one generation
       of Conways's game of life within the *inner cels* of
       that copy. The outer edge is always zero.'''
    newA = deepcopy(A)
    for row in range(1, len(newA)-1):
        for col in range(1, len(newA[0])-1):
             if countNeighbors(row, col, A) == 3:
                 newA[row][col] = 1
             if countNeighbors(row, col, A) < 2:
                 newA[row][col] = 0
             if countNeighbors(row, col, A) > 3:
                 newA[row][col] = 0
    return newA
############################################################
#part10
def interact():
'''Interact with a use to play Conway's Game of Life.'''
    line = raw_input("Enter Command:")
    line = line.replace(" ", "")
    while line[0] != "q":
        command = line[0]
        if command == 'n':
            evalA = eval(line[1:]) 
            x = evalA[0] 
            y = evalA[1] 
            A = createBoard(x,y)
        elif command == 'i':
            evalA2 = eval(line[1:])
            count = 0 
            for elements in range(len(evalA2)): 
                x = evalA2[count][0] 
                y = evalA2[count][1]  
                count += 1
                A[x][y] = 1
        elif command == 'p':
            printBoard(A)
        elif command == 'd':
            copyA = copy(A)
            name = [len(x) for x in copyA]
            w = name[0]
            h = len(copyA)
            for row in range(h):
                for col in range(w):
                    if A[row][col] == 1:
                        copyA[row][col] = "@"
                    elif A[row][col] == 0:
                        copyA[row][col] = " "
            printBoard(copyA)
        elif command == 'r':
            nextGen = line[1:]
            while nextGen != 0:
                A = next_life_generation(A)
                finalA = enter(w, h, A)
                evaluate -= 1 #decrement 
                printBoard(finalA)
        elif command == 'h':
            print "n-enter height width for the board"
            print "i-start life"
            print "p-print the board)"
            print "d-print the board after replacing 0s and 1s"
            print "r-show different generations for n times"
            print "h-help menu"
            print "q-quit"
        line = raw_input("Enter Command: ")
        line = line.replace(" ", "")
    print "Life is over\n"
############################################################
