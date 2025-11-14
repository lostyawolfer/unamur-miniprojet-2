import microbit
# import radio
"""
Choix:
------
Faire avec une liste de liste. 5X5

Choisis la direction avec l'inclinaison. A pour déplacer, B pour Lacher
"""



def create_new_pieces() -> bool:
    ...

def collide_with_others():
    ...

board = [[0]*5 for i in range(5)]
def get_board_image(board: list) -> microbit.Image:
    '''Create a microbit image object from the list[list[int]] format'''
    res = ''
    for i in board:
        for j in i:
            res += str(j)
        res += ':'
    return microbit.Image(res)
def get_board_list(board: microbit.Image) -> list:
    ...


def execute_order():
    ...

def get_random_piece():
    ...

def get_message_to_send_gamepad():
    ...

    """