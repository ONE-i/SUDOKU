def solveSudoku(board):
    emptyCell = findEmptyCell(board)
    # Goal
    # Check if all cell are done
    if not emptyCell:
        return True
    else:
        row, col = emptyCell

    # Fill in number 1-9 for empty cell
    for num in range(1, 10):
        # Check if the number is meet criteria
        # if true, set num to cell
        if checkCellNum(board, row, col, num):
            board[row][col] = num
            # move to the next cell
            if solveSudoku(board):
                return True
            # If no num fit, 
            # set previous cell back to 0
            board[row][col] = 0
    return False


def findEmptyCell(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return row, col


def checkCellNum(board, row, col, num):

    # Check if num duplicate in current row
    # Return False if yes
    if num in board[row]:
        return False

    # Check if num duplicate in current column
    # Return Flase if yes
    if num in [x[col] for x in board]:
        return False

    # Check if num duplicate in current block
    # Return False if yes
    blockRow = (row//3)*3 # Initial block row
    blockCol = (col//3)*3 # Initial block col
    for x in board[blockRow : blockRow + 3]:
        if num in x[blockCol : blockCol + 3]:
            return False

    # If nothing Flase
    # cell check passed
    return True



if __name__ == "__main__":

    testBoard = [
    [0, 8, 7, 0, 5, 0, 0, 3, 6],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 2, 3, 0, 0, 0, 4, 5],
    [0, 7, 3, 0, 1, 0, 0, 9, 0],
    [2, 9, 0, 5, 0, 4, 0, 7, 1],
    [0, 6, 0, 0, 8, 0, 3, 5, 0],
    [6, 2, 0, 0, 0, 3, 8, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [8, 4, 0, 0, 7, 0, 9, 2, 0]]

    if solveSudoku(testBoard):
        for i in testBoard:
            print(i)
    else:
        print('No Solution')
        for i in testBoard:
            print(i)

