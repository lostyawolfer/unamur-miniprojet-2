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
    del available_pieces[0] #enlève le cas où le carré est vide
    return available_pieces

def get_random_piece(available_pieces : list[list[list[int]]]) -> list[list[int]]:
    """
    Gives a random piece from the available_pieces list.

    Parameters:
    -----------
    available_pieces (list[list[list[int]]]): a list of the available pieces.

    Returns:
    -------
    piece (list[list[int]]) : A random piece of the available pieces.

    """
    return random.choice(available_pieces)


def combine_pieces_dropped_and_to_drop(board: list[list[int]], piece:list[list[int]]) -> bool:
    """
    Check if you can combine the already dropped pieces on the board to the piece to add. Then do it if it is possible.

    Parameters:
    -----------
    board (list[list[int]]) : the board containing the already dropped pieces, as 1s and 0s.
    piece(list[list[int]]) : the piece to combine with the board.

    Returns
    -------
    status (bool) : False if the operation can't be done, True if it can.
    """
    #Attention, il faut regarder si la pièce ne peut pas être mise plus à gauche ou plus à droite... Car [[0,0],[0,1]] existe par exemple
    position=[0, 0]
    if piece[0]==[0, 0]:
        position[1]=-1
    if piece[0][0]==piece[1][0]==0:
        position[0]=-1
    if check_place_for_piece(board, piece, position):
        place_piece(board, piece, position)
        return True
    return False



def check_place_for_piece(board: list[list[int]], piece: list[list[int]], coordonate: list[int]) -> bool:
    """
    Verifie if the piece can be placed in the board.

    Parameters
    ---------
    board (list[list[int]]) : the board we want to put the piece on
    piece (list[list[int]]) : the piece we want to put in the x, y coordonate
    coordonate (list[int]) : [x, y] being the coordonate of the top left of where we want to put the piece

    Returns:
    -------
    Status (bool): False if the board and piece overlap, True otherwhise
    """
    x0, y0 = coordonate  
    # loop over X et Y
    for y in range(len(piece)):
        for x in range(len(piece[0])):
            if piece[y][x] == 0:
                "do nothing"  #it's empty , nothing to do 
            else:
                if x0 + x < 0 or x0 + x >= len(board[0]) or y0 + y < 0 or y0 + y >= len(board):
                    return False
                if board[y0 + y][x0 + x] == 1:
                    return False
    return True

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
    x, y = coordonate
    
    for i,row in enumerate(piece):
        for j,cell in enumerate(row):
            if cell == 1:
                board[y + i][x + j] = 2


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
    result = ''
    for i in board:
        for j in i: #chaque liste une par une et puis chaque éléments un par un
            if j == 0:
                res += '0'
            elif j == 1:
                result += '9'
            else:
                result += '5' #pour la pièce à drop
        result += ':'
    return result


def execute_order(board : list[list[int]], order: str, score: int)->  tuple[bool,int]:
    """
    Execute one of the two order: "move [direction]" or "drop" on the piece to drop. Direction: left, right, up, down.
    And return a bool depending on the type of the event, and the final score.

    Parameters:
    -----------
    board (list[list[int]]) : the board with the piece to drop as 2, dropped as 1 and none as 0.
    order (str) : the order to be executed. "right", "left", "up", "down" or "drop".
    score (int) : the current score.

    Returns:
    --------                                                        
    done (bool): True if the order was to drop, False otherwise
    score (int): The new score, incremented if it was a drop.
    """
    #on peut utiliser des str.strip(order, " ") pour couper en deux à l'espace. Puis check si l'élément 1 de la string est move ou drop et si R ou L
    #utiliser les fonctions move() et drop()
    if order == "drop":
        drop(board)
        score+=1
        return True, score
        
    if order in ["up", "down", "left", "right"]:
        move(board, order)
        return False, score
    return False, score

def move(board: list[list[int]], direction: str) -> None:
    """
    Move the piece to drop to the left L or to the right R. Does nothing if the piece can't be moved.

    Parameters:
    ----------
    board (list[list[int]]) : the board with the piece to drop as 2, dropped as 1 and none as 0.
    direction (str) : the direction to move the piece to drop, "L" or "R" or "D" or "U".

    Returns:
    -------
    None
    """

    if can_be_move(board,direction)==True :
        position=[]
        #checking all the elements:
        for row_index,row in enumerate(board):
                for col_index,cell in enumerate(row):
                        #stock stocks the piece list in the previous empty list (positoin):                      
                        if cell==2:
                            position.append((row_index,col_index))
        #cleans the place where were the pieces:
        for (a,b) in position:
             board[a][b]=0
        #moved to wanted destination:
        vector=[0, 0]
        for (a,b) in position:
            if direction=="left":
                vector[0]=-1
            elif direction=="right":
                vector[0]=+1
            elif direction=="down":
                vector[1]=+1
            else: #if it is "up"
                vector[1]=-1
            board[a+vector[1]][b+vector[0]]=2

def can_be_move(board: list[list[int]], direction: str) -> bool:
    """
    Check if we can move the piece to drop to the left, right, up or down.

    Parameters:
    ----------
    board (list[list[int]]) : the board with the piece to drop as 2, dropped as 1 and none as 0.
    direction (str) : the direction to move the piece to drop, "left", "right", "up" or "down".

    Returns:
    -------
    result (bool): True if it can be moved, False otherwise
    """
    if direction =="left":
        vector=[0, -1]
    elif direction=="right":
        vector=[0, +1]
    elif direction=="up":
        vector=[-1, 0]
    else:
        vector=[1, 0] #si c'est down

    for row_position, row in enumerate(board):
        for collomn_positionn, element in enumerate(row):
            if element==2:
                try:
                    if board[row_position+vector[0]][collomn_positionn+vector[1]] == 1:
                        return False #si il y a un 1 là où on veut aller, alors on dis qu'on peut pas bouger
                except:
                    return  False #si la case est hors du board
    return True


def drop(board: list[list[int]]) -> None:
    """
    Set the piece as a dropped piece.

    Parameters:
    -----------
    board (list[list[int]]) : the board with the piece to drop as 2, dropped as 1 and none as 0.

    Returns:
    --------
    None
    """
    for row_index,row in enumerate(board):
        for col_index,cell in enumerate(row):
            if cell==2:
                board[row_index][col_index]=1


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
    game_is_over= not combine_pieces_dropped_and_to_drop(board, new_piece)

    if not game_is_over:
        #ask orders until the current piece is dropped
        piece_dropped=False
        while not piece_dropped:
            #send state of the board to the gamepad (as a string)
            radio.send(board_status_to_send(board))

            #wait until gamepad send an order
            order = get_message()

            #execute order (drop or move piece)
            piece_dropped, nb_dropped_pieces=execute_order(board, order, nb_dropped_pieces)
        #wait a few milliseconds and clear the screen
        microbit.sleep(500)
        microbit.display.clear()

#Tell that the game is over
microbit.display.scroll("Game is over", delay=100)