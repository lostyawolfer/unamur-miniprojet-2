"""
TO DELETE WHEN CODE DONE

Choix:
------
Faire avec une liste de liste. 5X5

Choisis la direction avec l'inclinaison. A pour déplacer, B pour Lacher


def create_new_pieces() -> bool:
    ...

def collide_with_others():
    ...

board = [[0]*5 for i in range(5)]

def execute_order():
    ...

def get_random_piece():
    ...

def get_message_to_send_gamepad():
    ...


def get_board_image(board: list[list[int]]) -> microbit.Image:
    '''Create a microbit image object from the list[list[int]] format'''
    res = ''
    for i in board:
        for j in i:
            if j == 0:
                res += '0'
            elif j == 1:
                res += '9'
            else:
                res += '5'
        res += ':'
"""

import math
import random
import microbit
import radio

#définition de fonction
def get_message():
    message=None
    while message==None:
        microbit.sleep(250)
        message=radio.recieve()
    return message

def create_empty_board(size : int) -> list[list[int]]:
    """
    Create and return a list of list of zeros, aka a square matrice of size size, full of 0s

    Parameters:
    -----------
    size(int): The size of the lists, or of the square matrice

    Returns:
    --------
    Square_matrice (list[list[int]]): the matrice/list of list created
    """
    list0=[[0]*size for i in range(size)]
    return list0

def get_available_pieces() -> list[list[list[int]]]:
    """
    Create a list of all the available pieces. These are 2x2 or 1x1 pieces. The pieces are stocked in a square
    matrice of size 2x2, with 1 where there is a block and 0 if not.

    Parameters:
    -----------
    None

    Returns:
    --------
    available_pices (list[list[list[int]]]) : a list of the available pieces.
    """
    available_pieces=[]
    #créer toutes les possibilités
    for square1 in range(2):
        for square2 in range(2):
            for square3 in range(2):
                for square4 in range(2):
                    available_pieces+=[[[square1, square2], [square3, square4]]] #ajoute à la liste, le 
                    #carrée en tant que un seul élément
    del available_pieces[0], available_pieces[2] #enlève le cas où le carré est vide
    return available_pieces

def get_random_piece(available_pieces : list[list[list[int]]]) -> list[list[int]]:
    """
    Gives a random piece from the available_piece list.

    Parameters:
    -----------
    available_pieces (list[list[list[int]]]): a list of the available pieces, in a 2x2 square matrice.

    Returns:
    -------
    piece (list[list[int]]) : A random piece of the available pieces.

    """
    ...


def combine_pieces_dropped_and_to_drop(board: list[list[int]], piece:list[list[int]]) -> bool:
    """
    Check if you can combine the already dropped pieces on the board to the piece to add. Then do it if it is possible.

    Parameters:
    -----------
    board (list[list[int]]) : the board containing the already dropped pieces, as 1s and 0s.
    piece(list[list[int]]) : the piece to combine with the board.

    Returns
    -------
    status (bool) : False if the operation can't be done, True if it is done.
    """
    #Attention, il faut regarder si la pièce ne peut pas être mise plus à gauche ou plus à droite... Car [[0,0],[0,1]] existe par exemple
    ...

def check_place_for_piece(board : list[list[int]], piece : list[list[int]], coordonate: list[int]) -> bool:
    """
    Check if a piece can be placed on the board in the (x, y) coordonate, starting from the top left.

    Parameters:
    -----------
    board (list[list[int]]) : the board we want to put the piece on
    piece (list[list[int]]) : the piece we want to put in the x, y coordonate
    coordonate (list[int]) : [x, y] being the coordonate of the top left of where we want to put the piece

    Returns:
    -------
    Status (bool): False if the board and piece overlap, True otherwhise
    """
    #Bien vérifier si un "1" ne sort pas de board, mais les 0 peuvent.
    ...

def place_piece(board : list[list[int]], piece : list[list[int]], coordonate: list[int]) -> None:
    """
    Places the piece on the board and the given coordonates

    Parameters:
    ----------
    board (list[list[int]]) : the board we want to put the piece on
    piece (list[list[int]]) : the piece we want to put in the x, y coordonate
    coordonate (list[int]) : [x, y] being the coordonate of the top left of where we want to put the piece

    returns:
    -------
    None
    """
    ...


def board_status_to_send(board : list[list[int]]) -> str:
    """
    Create a string from the board aimed to be sent by radio to the gamepad. 0 when there is no pieces, 5 when there is a piece
    dropped and 9 for the piece to drop, with a ":" to separate every row of the list.

    Parameters:
    -----------
    board (list[list[int]]) : the current state of the board

    returns:
    --------
    result (str): a string representing the state of the board, ready to be send. 

    """
    #voir code de Kostiantyn en commentaire plus haut. Just ne pas transformer on objet image
    ...


def execute_order(board : list[list[int]], order: str)-> bool:
    """
    Execute one of the two order: "move [direction]" or "drop" on the piece to drop. Direction: L for left and R for right.
    And return a bool depending on the type of the event.

    Parameters:
    -----------
    board (list[list[int]]) : the board with the piece to drop as 2, dropped as 1 and none as 0.
    order (str) : the order to be executed. "move R", "move L" or "drop".

    Returns:
    --------
    done (bool): True if the order was to drop, False otherwise
    """
    #on peut utiliser des str.strip(order, " ") pour couper en deux à l'espace. Puis check si l'élément 1 de la string est move ou drop et si R ou L
    #utiliser les fonctions move() et drop()
    ...

def move(board: list[list[int]], direction: str) -> None:
    """
    Move the piece to drop to the left L or to the right R. Does nothing if the piece can't be moved.

    Parameters:
    ----------
    board (list[list[int]]) : the board with the piece to drop as 2, dropped as 1 and none as 0.
    direction (str) : the direction to move the piece to drop, "L" or "R".

    Returns:
    -------
    None
    """
    #utiliser can_be_move(), puis le faire si return True
    ...

def can_be_move(board: list[list[int]], direction: str) -> bool:
    """
    Check if we can move the piece to drop to the left L or to the right R or B to the bottom.

    Parameters:
    ----------
    board (list[list[int]]) : the board with the piece to drop as 2, dropped as 1 and none as 0.
    direction (str) : the direction to move the piece to drop, "L" or "R" or "B".

    Returns:
    -------
    result (bool): True if it can be moved, False otherwise
    """
    ...

def drop(board: list[list[int]]) -> None:
    """
    Drops the piece to drop to the lowest it can be. Also set the piece as a dropped piece.

    Parameters:
    -----------
    board (list[list[int]]) : the board with the piece to drop as 2, dropped as 1 and none as 0.

    Returns:
    --------
    None
    """
    #utiliser can_be_move(board, "B")
    ...


#settings
group_id=27

#setup radio recieve order
radio.on()
radio.config(group=group_id)

#create empty board + available pieces
board=create_empty_board(5)
available_pieces=get_available_pieces()

#loop until game is over
nb_dropped_pieces=0
game_is_over=False

while not game_is_over:
    #show score
    microbit.display.show(nb_dropped_pieces)

    #create a new piece in the top left corner
    new_piece=get_random_piece(available_pieces)
    
    #check if new piece collides with dropped pieces
    game_is_over=combine_pieces_dropped_and_to_drop(board, new_piece)

    if not game_is_over:
        #ask orders until the current piece is dropped
        piece_dropped=False
        while not piece_dropped:
            #send state of the board to the gamepad (as a string)
            radio.send(board_status_to_send(board))

            #wait until gamepad send an order
            order = get_message()

            #execute order (drop or move piece)
            piece_dropped=execute_order(board, order)
        #wait a few milliseconds and clear the screen
        microbit.sleep(500)
        microbit.display.clear()

#Tell that the game is over
microbit.display.scroll("Game is over", delay=100)