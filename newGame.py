from sudokuSolver import solveSudoku
from copy import deepcopy

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


def newGame():
    playerBoard = testBoard # Add board generator here
    resultBoard = deepcopy(playerBoard)
    solveSudoku(resultBoard)
    return playerBoard, resultBoard

