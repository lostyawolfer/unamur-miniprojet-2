"""
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

#...................
#...................

#settings
group_id=27

#setup radio recieve order
radio.on()
radio.config(group=group_id)

#create empty board + available pieces
#......................

#loop until game is over
nb_dropped_pieces=0
game_is_over=False

while not game_is_over:
    #show score
    microbit.display.show(nb_dropped_pieces)

    #create a new piece in the top left corner
    #..................
    
    #check if new piece collides with dropped pieces
    #game_is_over=.............

    if not game_is_over:
        #ask orders until the current piece is dropped
        piece_dropped=False
        while not piece_dropped:
            #send state of the board to the gamepad (as a string)
            #radio.send(......)

            #wait until gamepad send an order
            order = get_message()

            #execute order (drop or move piece)
            #................
        #wait a few milliseconds and clear the screen
        microbit.sleep(500)
        microbit.display.clear()

#Tell that the game is over
microbit.display.scroll("Game is over", delay=100)