"""
Choix:
------
Faire avec une liste de liste. 5X5

Choisis la direction avec l'inclinaison. A pour déplacer, B pour Lacher

def create_new_pieces() -> bool:
    ...

def collide_with_others():
    ...

def execute_order():
    ...

def get_random_piece():
    ...

def get_message_to_send_gamepad():
    ...





board = [[0]*5 for i in range(5)]

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
    return microbit.Image(res)
    
def get_board_list(board: microbit.Image) -> list[list[int]]:
    '''Create a list[list[int]] format from a microbit image object'''
    ... # TODO: make this function
    

"""

import microbit
import radio

#definition of functions
def get_message():
    message=None
    while message==None:
        microbit.sleep(250)
        message=radio.recieve()
    return message

#...................
#...................

#settings
group_id=27

#setup radio recieve order
radio.on()
radio.config(group=group_id)

#loop forever (until micro:bit is switched off)
while True:
    #get view of the board
    view=get_message()

    #clear screen
    microbit.display.clear()

    #show view of the board
    #................

    #wait for button A or B to be pressed
    while not(microbit.button_a.is_pressed() or microbit.button_b.is_pressed()):
        microbit.sleep(50)

        if microbit.button_a.is_pressed():
            #send current direction
            #..................
            #..................
            ...
        
        elif microbit.button_b.is_pressed():
            #notify the piece should be dropped
            #radio.send(..........)
            ...
