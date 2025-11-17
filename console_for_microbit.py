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
    list0=[[0]*size for i in range(size)]
    return list0

def get_available_pieces() -> list[list[list[int]]]:
    available_pieces=[]
    for square1 in range(2):
        for square2 in range(2):
            for square3 in range(2):
                for square4 in range(2):
                    available_pieces+=[[[square1, square2], [square3, square4]]]
    del available_pieces[0]
    return available_pieces

def get_random_piece(available_pieces : list[list[list[int]]]) -> list[list[int]]:
    return random.choice(available_pieces)


def combine_pieces_dropped_and_to_drop(board: list[list[int]], piece:list[list[int]]) -> bool:
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
    x0, y0 = coordonate
    for y in range(len(piece)):
        for x in range(len(piece[0])):
            if piece[y][x] == 0:
                "do nothing"
            else:
                if x0 + x < 0 or x0 + x >= len(board[0]) or y0 + y < 0 or y0 + y >= len(board):
                    return False
                if board[y0 + y][x0 + x] == 1:
                    return False
    return True

def place_piece(board : list[list[int]], piece : list[list[int]], coordonate: list[int]) -> None:
    x, y = coordonate
    
    for i,row in enumerate(piece):
        for j,cell in enumerate(row):
            if cell == 1:
                board[y + i][x + j] = 2


def board_status_to_send(board : list[list[int]]) -> str:
    result = ''
    for i in board:
        for j in i:
            if j == 0:
                res += '0'
            elif j == 1:
                result += '9'
            else:
                result += '5'
        result += ':'
    return result


def execute_order(board : list[list[int]], order: str, score: int)->  tuple[bool,int]:
    if order == "drop":
        drop(board)
        score+=1
        return True, score
        
    if order in ["up", "down", "left", "right"]:
        move(board, order)
        return False, score
    return False, score

def move(board: list[list[int]], direction: str) -> None:

    if can_be_move(board,direction)==True :
        position=[]
        for row_index,row in enumerate(board):
                for col_index,cell in enumerate(row):                    
                        if cell==2:
                            position.append((row_index,col_index))
        for (a,b) in position:
             board[a][b]=0
        vector=[0, 0]
        for (a,b) in position:
            if direction=="left":
                vector[0]=-1
            elif direction=="right":
                vector[0]=+1
            elif direction=="down":
                vector[1]=+1
            else:
                vector[1]=-1
            board[a+vector[1]][b+vector[0]]=2

def can_be_move(board: list[list[int]], direction: str) -> bool:
    if direction =="left":
        vector=[0, -1]
    elif direction=="right":
        vector=[0, +1]
    elif direction=="up":
        vector=[-1, 0]
    else:
        vector=[1, 0]

    for row_position, row in enumerate(board):
        for collomn_positionn, element in enumerate(row):
            if element==2:
                try:
                    if board[row_position+vector[0]][collomn_positionn+vector[1]] == 1:
                        return False
                except:
                    return  False
    return True


def drop(board: list[list[int]]) -> None:
    for row_index,row in enumerate(board):
        for col_index,cell in enumerate(row):
            if cell==2:
                board[row_index][col_index]=1


group_id=27

radio.on()
radio.config(group=group_id)

board=create_empty_board(5)
available_pieces=get_available_pieces()

nb_dropped_pieces=0
game_is_over=False

while not game_is_over:
    microbit.display.show(nb_dropped_pieces)

    new_piece=get_random_piece(available_pieces)
    
    game_is_over= not combine_pieces_dropped_and_to_drop(board, new_piece)

    if not game_is_over:
        piece_dropped=False
        while not piece_dropped:
            radio.send(board_status_to_send(board))

            order = get_message()

            piece_dropped, nb_dropped_pieces=execute_order(board, order, nb_dropped_pieces)
        microbit.sleep(500)
        microbit.display.clear()

microbit.display.scroll("Game is over", delay=100)