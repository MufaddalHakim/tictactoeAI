"""
Tic Tac Toe Player
"""

import math
import copy

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
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                count += 1
    
    if count % 2 == 1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range (3):
        for j in range(3):
            if board[i][j] == None:
                actions.add((i, j))

    return actions                    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """    
    move = player(board)
    boardCopy = copy.deepcopy(board)
    if move == X:
        boardCopy[action[0]][action[1]] = "X"
    else:
        boardCopy[action[0]][action[1]] = "O"
    
    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """    
    for i in range(3):
        if board[i][2] == board[i][1] == board[i][0]:
            return board[i][2]    
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[1][j]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]    
    
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != None:
                count += 1

    if winner(board) is not None:
        return True
    elif count == 9:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = 0
    n = winner(board)
    if n == 'X':
        win = 1
    elif n == 'O':
        win = -1        

    return win


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """    

    if terminal(board):
        return None

    else:
        if player(board) == X:
            v = -math.inf
            best = None
            for action in actions(board):
                # if min_value(result(board, action)) > v:
                aux = min_value(result(board, action))
                if aux > v:
                    v = aux
                    best = action

            return best

        elif player(board) == O:
            v = math.inf
            best = None
            for action in actions(board):
                # if max_value(result(board, action)) < v:
                aux = max_value(result(board, action))
                if aux < v:
                    v = aux
                    best = action

            return best

def max_value(board):

    v = -math.inf 

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v
        

def min_value(board):

    v = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action)))            

    return v
    
