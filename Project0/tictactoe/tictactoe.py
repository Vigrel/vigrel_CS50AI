"""
Tic Tac Toe Player
"""
import random
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
    counter = 0
    for i in board:
        counter += i.count(EMPTY)
    if counter % 2 == 0:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row in range(len(board)):
        for cell in range(len(board[row])):   
            if board[row][cell] == EMPTY:
                possible_actions.add((row, cell))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise NotImplementedError   
    elif action not in actions(board):
        raise NotImplementedError
    else:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    xwin = [X,X,X]
    owin = [O,O,O]
    win_position = [[board[0][0],board[0][1],board[0][2]], 
                    [board[1][0],board[1][1],board[1][2]],
                    [board[2][0],board[2][1],board[2][2]],
                    [board[0][0],board[1][0],board[2][0]],
                    [board[0][1],board[1][1],board[2][1]],
                    [board[0][2],board[1][2],board[2][2]],
                    [board[0][0],board[1][1],board[2][2]],
                    [board[0][2],board[1][1],board[2][0]]]
    for win in win_position:
        if win == xwin:
            return X
        elif win == owin:
            return O

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win_state = winner(board)
    
    if win_state != None:
        return True

    for row in board:
        for cell in row:   
            if cell == EMPTY:
                return False
    return True
            

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_utility = winner(board)

    if win_utility == X:
        return 1
    
    elif win_utility == O:
        return -1
    
    else:
        return 0

def max_value(state):

    if terminal(state):
        return utility(state)
        
    v = - math.inf

    for action in actions(state):
       v = max(v, min_value(result(state, action)))
    return v

def min_value(state):
    if terminal(state):
        return utility(state)
    v = math.inf
    for action in actions(state):
       v = min(v, max_value(result(state, action)))
    return v




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state():
        return (1,1)

    if player(board) == X:
        v = - math.inf
        optimal_action = None
        for action in actions(board):    
            if min_value(result(board,action)) > v:
                v = min_value(result(board,action))
                optimal_action = action   
            
    else:
        v = math.inf
        optimal_action = None
        for action in actions(board):    
            if max_value(result(board,action)) < v:
                v = max_value(result(board,action))
                optimal_action = action   
    
    return optimal_action
