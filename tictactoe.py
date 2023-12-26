"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = 0
    O_count = 0
    for row in board:
        X_count += row.count(X)
        O_count += row.count(O)
        if X_count <= O_count:
            return X
        else:
            return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleMoves = set()
    for rowIndex, row in enumerate(board):
        for colIndex, item in enumerate(row):
            if item == None:
                possibleMoves.add((rowIndex,colIndex))
    return possibleMoves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    playerMove = player(board)
    newBoard = deepcopy(board)
    i, j = action
    if board[i][j] != None:
        raise Exception
    else:
        newBoard[i][j] = playerMove
    return newBoard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, O):
        for row in board:
            if row == [player] * 3:
                return player
        for i in range(3):
            column = [board[x][i] for x in range(3)]
            if column == [player] * 3:
                return player
        if [board[i][i] for i in range(0, 3)] == [player] * 3:
            return player
        elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
            return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winPlayer = winner(board)
    if winPlayer == X:
        return 1
    elif winPlayer == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        optimalMove = ()
        if terminal(board):
            return utility(board), optimalMove
        else:
            v = -5
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimaMove = action
            return v, optimalMove
    
    def min_value(board):
        optimalMove = ()
        if terminal(board):
            return utility(board), optimalMove
        else:
            v = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimalMove = action
            return v, optimalMove
        
    curr_player = player(board)
    if terminal(board):
        return None
    if curr_player == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
    
