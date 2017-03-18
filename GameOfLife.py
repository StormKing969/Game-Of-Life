import sys
import random

# This functio was given
def createOneRow(width):
    """returns one row of zeros of width "width" ..
        You might use this in your createBoard(width, height) function"""
    row = []
    for col in range(width):
        row += [0]
    return row

# This function was given with a changed made to it
# Test:
# EX: A = createBoard(3,5) returns [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
def createBoard(height, width):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]   
    return A

# This fucntion was given
# Test:
# Ex: A = createBoard(3,5)
# printBoard(A) =
# 00000
# 00000
# 00000
def printBoard( A ):
    """ this function prints the 2d list-of-lists
        A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
        
# This function was made by understanding that row == col
# and when they equal at the same point then it creates a
# diagonal
# Test: A = diagonalize(7,6)
# Ex:
# 100000
# 010000
# 001000
# 000100
# 000010
# 000001
# 000000
def diagonalize(height,width):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( height, width)
    
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

# This function was created when I understood that
# range you can implement restrictions so that
# you can have the rest of the cells on the outside be 0.
# Test: A = innerCells(7,6)
# printBoard(A)
# 000000
# 011110
# 011110
# 011110
# 011110
# 011110
# 000000
def innerCells(height, width):
    """takes a width and a height and gives inner cells for the game of Life"""
    
    A = createBoard( height, width)

    for row in range(1,height-1):
        for col in range(1,width-1):
                A[row][col] = 1
    return A

# This function returns a random cell living or dead
# and the random cell is put into a new board
# Test:
# Ex: A = randomCells(7,6)
# printBoard(A)
# 000000
# 000100
# 010100
# 010000
# 000000
# 001100
# 000000
def randomCells(height, width):
    """takes a width and a height and gives a randomly generated array assigned
        of 1's and 0's"""
    A = createBoard(height,width)
    
    for row in range(1,height-1):
        for col in range(1,width-1):
                A[row][col] = random.choice([0,1])
    return A

# This function is very similar to innerReverse since I did innerReverse
# before creating this function and used a similar concept to copy the
# board
# Test:
# Ex: oldA = createBoard(2,2)
# printBoard(oldA)
# 00
# 00
# newA = copy(oldA)
# printBoard(newA)
# 00
# 00
# oldA[0][0] = 1
# printBoard(oldA)
# 10
# 00
# printBoard(newA)
# 00
# 00

def copy(a):
    """This makes a copy of the orginalBoard and returns it"""
    b = [len(x) for x in a]
    w = b[0]
    h = len(a)
    K = createBoard(h,w)
    for row in range(1,h-1):
        for col in range(1,w-1):
            if a[row][col] == 1:
                K[row][col] = 1
            else:
                K[row][col] = 0
    return K

# This function reverses the inside of the board
# I figured out how to extract information to get the lenght
# and the width of the board so I could create a new board
# and reverse everything
# Test:
# Ex: A = randomCells(8,8)
# printBoard(A)
# 00000000
# 01111000
# 01000100
# 01111000
# 00111000
# 01111010
# 00101110
# 00000000
# g = innerReverse(A)
# printBoard(g)
# 00000000
# 00000110
# 00111010
# 00000110
# 01000110
# 00000100
# 01010000
# 00000000
def innerReverse(A):
    """Replaces the inner values by replacing them with their opposite."""
    b = [len(x) for x in A]
    w = b[0]
    h = len(A)
    K = createBoard(h,w)
    for row in range(1,h-1):
        for col in range(1,w-1):
            if A[row][col] == 1:
                K[row][col] = 0
            else:
                K[row][col] = 1
    return K

# This function is supposed to count the neighbors surroundng
# the main cell. I figured out that its very similar to a X Y
# graph and I could subtract x - 1 and y - 1 to get diagonals
# and I could get the rest like that. I had issues with index
# out of bound errors but made preventative measures to stop it
# by checking every time. Every time i check it made sure if it
# is an empty list.


def countNeighbors( row, col, A ):
    """Counts how many neighbors a point on the board has."""
    count = 0
    if A[row][col-1] != []:
        if A[row][col-1] == 1:
            count += 1
    if A[row+1][col-1] != []:
        if A[row+1][col-1] == 1:
            count += 1
    if A[row+1][col] != []:
        if A[row+1][col] == 1:
            count += 1
    if A[row+1][col+1] != []:
        if A[row+1][col+1] == 1:
            count += 1
    if A[row][col+1] != []:
        if A[row][col+1] == 1:
            count += 1
    if A[row-1][col+1] != []:
        if A[row-1][col+1] == 1:
            count += 1
    if A[row-1][col] != []:
        if A[row-1][col] ==  1:
            count += 1
    if A[row-1][col-1] != []:
        if A[row-1][col-1] == 1:
            count += 1
    return count

# The purpose of this function is to calculate the next generation
# it took me a while to interpret the rules and apply them to
# the function. The helper function came in handy.
# Test:
# EX: A = [ [0,0,0,0,0],
#      [0,0,1,0,0],
#      [0,0,1,0,0],
#      [0,0,1,0,0],
#      [0,0,0,0,0]]
# printBoard(A)
# 00000
# 00100
# 00100
# 00100
# 00000
# A2 = next_life_generation(A)
# printBoard(A2)
# 00000
# 00000
# 01110
# 00000
# 00000
def next_life_generation( A ):
    """ makes a copy of A and then advanced one
        generation of Conway's game of life within
        the *inner cells* of that copy.
        The outer edge always stays 0.
    """
    height = len(A)
    width = len(A[0])
    newA = copy(A)
    for row in range(height):
       if row == 0 or row == height - 1:
           for col in range(width):
               newA[row][col] = 0
       else:
           for col in range(width):
               if col == 0 or col == width - 1:
                   newA[row][col] = 0
               else:
                   if A[row][col] == 0 and countNeighbors(row,col,A) == 3:
                        newA[row][col] = 1
                   elif countNeighbors(row,col,A) < 2:
                        newA[row][col] = 0
                   elif countNeighbors(row,col,A) > 3:
                        newA[row][col] = 0
    return newA

# This Functions purpose is to convert to " " and @
# This was a simple conversion that did not take long
# since it was just iterating through the array and switching
# 1's and 0's to " " and "@" symbols

def convert(A):
    A1 = copy(A)
    b = [len(x) for x in A1]
    w = b[0]
    h = len(A1)
    for row in range(h):
        for col in range(w):
            if A1[row][col] == 1:
                A1[row][col] = "@"
            else:
                A1[row][col] = " "
    return A1

# This Functions purpose is to add interaction between the user
# and creates the game of life. The commands were
# first hard to understand and then once I figured out
# that I could use eval to evaluate the string
# Test:
# interact()
# Enter Command: n [10,20]
# Enter Command: p
# 00000000000000000000
# 00000000000000000000
# 00000000000000000000
# 00000000000000000000
# 00000000000000000000
# 00000000000000000000
# 00000000000000000000
# 00000000000000000000
# 00000000000000000000
# 00000000000000000000
# Enter Command: i [[4,6],[4,7],[4,8],[4,9],[5,9],[6,9],[7,9],[8,9]]
# Enter Command: d
#                     
#                    
#                    
#                    
#      @@@@          
#         @          
#         @          
#         @          
#         @
# Enter Command: h
# Commands:
#    n      [height,width] (Create a height * width board)
#    i      (initialize life)
#    p      (print the board)
#    d      (display the board)
#    r      (advance n generations, displaying each after)
#    h      (display this help reminder)
#    q      (quit)
# Enter Command: r 4
#                     
#                    
#                    
#       @@           
#       @@@          
#       @ @@         
#        @@@         
#        @@@
#
#                    
#       @ @          
#      @   @         
#       @            
#       @   @        
#        @ @         
#         @          
#
#                     
#                    
#      @@@           
#      @@            
#       @@           
#        @@@         
#         @          
# 
#
#                    
#       @            
#      @ @           
#                    
#      @             
#       @  @         
#        @@@         
# 
# Enter Command: q
# Life is over

def interact():
    """ Interact with a user to play Conway's Game of Life.
    """
    A = None
    line = raw_input("Enter Command: ")
    line = line.replace(" ", "")
    while line[0] != "q":
        command = line[0]
        if command == 'n':
            line = line.replace(" ","")
            line = line[1:]
            coor = eval(line)
            A = createBoard(coor[0],coor[1])
        elif command == 'i':
            line = line.replace(" ","")
            line = line[1:]
            count = len(eval(line))
            start = 0
            coor = eval(line)
            while start <= count -1:
                row = coor[start][0]
                col = coor[start][1]
                A[row][col] = 1
                start += 1
        elif command == 'p':
            printBoard(A)
        elif command == 'r':
            line = line.replace(" ","")
            line = line[1:]
            g = eval(line)
            while g != 0:
                A = next_life_generation(A)
                A2 = convert(A)
                g += -1
                printBoard(A2)
                print("\n")
        elif command == 'd':
            A1 = convert(A)
            printBoard(A1)
        elif command == "h":
            print("""Commands:
    n      [height,width] (Create a height * width board)
    i      (initialize life)
    p      (print the board)
    d      (display the board)
    r      (advance n generations, displaying each after)
    h      (display this help reminder)
    q      (quit)""")
        line = raw_input("Enter Command: ")
        line = line.replace(" ", "")
    print "Life is over\n"
