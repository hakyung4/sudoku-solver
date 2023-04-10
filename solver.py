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

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            # printing horizontal line
            print("- - - - - - - - - - - - - ")
        # len(board[0]) : length of each row
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(board[i][j])
            
            else:
                print(str(board[i][j]) + " ", end="")

# Given a board, find an empty square position.
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col
            
    return None

# Given the board, check if the current board is valid.
def valid(board, num, pos):
    # check row
    for i in range(len(board[0])):
        # check each element in the row and see if it's equal to the number that it tried. and if it's the position that it just inserted, ignore that pos.
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    # check col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    # check the square
    # First, determine which box it's in.
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # loop through the box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

# recursive
def solve(board):
    # Base case: the board is solved; full.
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

print_board(board)
solve(board)
print("------------------------------")
print_board(board)
