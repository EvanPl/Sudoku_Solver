#Sudoku Game
#Date Created: 18/09/21
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#print (len(board)) #number of rows
#print (len(board[0])) #number of columns

#Function that prints the sudoku board in a presentable format
def print_board (sudoku):
    for i in range(len(sudoku)):
        if i % 3 == 0 and i!=0:
            print("- - - - - - - -")
        for j in range (len(sudoku[0])):
            if (j % 3) == 0 and j!=0:
                print (" | ", end="")
            if j==len(sudoku[0])-1:
                    print(sudoku[i][j])
            else:
                    print(sudoku[i][j], end="")

#Function that find an empty element in the board (zero in our case)
def find_empty (sudoku):
    for i in range (len(sudoku)):
        for j in range (len(sudoku[0])):
            if (sudoku[i][j]==0):
                return (i,j)

def valid (sudoku, num, pos):
    for j in range (len(sudoku[0])):
        if sudoku[pos[0]][j] ==num and pos[1]!=j:
            return False

    for i in range (len(sudoku)):
        if sudoku[i][pos[1]] == num and pos[0]!=i:
            return False

    box_x= pos [0] // 3
    box_y= pos [1] // 3

    for i in range (box_x*3, box_x*3+3):
        for j in range (box_y*3,box_y*3+3):
            if sudoku[i][j] == num and (i,j)!=pos:
                return False
    return True

def solver (sudoku):
    find = find_empty(sudoku)
    #base case of recursion
    if not find:
        return True
    else:
        row, column = find
    for i in range (1,10):
        if valid (sudoku, i , (row,column)):
            sudoku[row][column]=i
            #print ("*************")
            #print_board(sudoku) Use this command to see all the steps towards the solution
            if solver(sudoku):

                return True
            sudoku[row][column]=0
    return False

print("Sudoku board to be solved")
print_board(board)
if (solver(board)):
    print("Solution: ")
    solver(board)
    print_board(board)
else:
    print ("No solution found - check the sudoku board again")