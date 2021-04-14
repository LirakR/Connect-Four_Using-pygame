import numpy as np

board_rows = 6
board_col = 7
board = np.zeros((board_rows, board_col))


def create_board():
    return board



# Metoda qe luan lojtarin(1 ose 2) ne kolonen e caktuar
def play_here(array, player, column):
    if column ==-1:
        return 
    column = column - 1
    if array[-1][column] == 0:
        array[-1][column] = player
    else:
        for i in range(board_rows-1):
            if array[i+1][column] != 0 and array[i][column]==0:
                array[i][column] = player

def is_four_horizontal(array):
    for i in range(0, board_rows):
        for j in range(0, board_col - 3):
            if array[i][j] == array[i][j + 1] == array[i][j + 2] == array[i][j + 3] != 0:
                return True
    return False


def is_four_vertical(array):
    for i in range(0, board_rows - 3):
        for j in range(0, board_col):
            if array[i][j] == array[i + 1][j] == array[i + 2][j] == array[i + 3][j] != 0:
                return True
    return False


def is_four_diagonal_down(array):
    for i in range(0, board_rows - 3):
        for j in range(0, board_col - 3):
            if array[i][j] == array[i + 1][j + 1] == array[i + 2][j + 2] == array[i + 3][j + 3] != 0:
                return True
    return False


def is_four_diagonal_up(array):
    for i in range(3, board_rows):
        for j in range(0, board_col-3):
            if array[i][j] == array[i - 1][j + 1] == array[i - 2][j + 2] == array[i - 3][j + 3] != 0:
                return True
    return False

def check_winner(array):
    if is_four_horizontal(array) or is_four_vertical(array) or is_four_diagonal_up(array) or is_four_diagonal_down(array):
        return True
    return False

def get_board():
    return board


def get_rows():
    return board_rows


def get_columns():
    return board_col

def check_zeros_in_column(array, column):
    for i in range(len(array[0])-1):
        if array[i][column-1]==0:
            return False
    return True

def clear_board():
    return np.zeros((6, 7))


boardTEST =[
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [2, 1, 0, 1, 0, 0, 1],
        [2, 2, 1, 0, 0, 1, 1],
        [2, 2, 2, 1, 0, 1, 1]
    ]

