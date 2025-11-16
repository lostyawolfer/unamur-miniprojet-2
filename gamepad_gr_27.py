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

# definition of functions
def get_message():
    message=None
    while message==None:
        microbit.sleep(250)
        message=radio.receive()
    return message

def get_tilt() -> str | None:
    """
    Gets current BBC micro:bit's general tilt direction.

    Returns string ['up', 'down', 'left', 'right'] if a direction is detected,
    None if no tilt or the tilt directions are ambiguous (exactly equal).
    """
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()

    # tilt directions:
    #
    #       up
    #        ^ +y
    #        |
    # left   |    right
    # -x ----+---> +x
    #        |
    #        |
    #        | -y
    #       down

    if abs(x) > abs(y):
        return 'right' if y > 0 else 'left'
        # if x=0 then either the y coordinate part of condition is triggered,
        # or they both are 0, meaning they are equal, which goes to "else", returning None

    elif abs(y) > abs(x):
        return 'up' if y > 0 else 'down'
        # if y=0 then either the x coordinate part of condition is triggered,
        # or they both are 0, meaning they are equal, which goes to "else", returning None

    else:
        return None

##################### ATTENTION: TO BE DELETED #####################
### temporary function, to be deleted on final project upload
### allows to check the integrity of tilt direction readings
def show_tilt_on_screen() -> None:
    """Shows an arrow in the direction of current tilt, or a cross if no tilt is detected."""
    tilt = get_tilt()
    if tilt == 'right':
        microbit.display.show(microbit.Image('00900:'
                                             '00990:'
                                             '99999:'
                                             '00990:'
                                             '00900'))
    elif tilt == 'left':
        microbit.display.show(microbit.Image('00900:'
                                             '09900:'
                                             '99999:'
                                             '09900:'
                                             '00900'))
    elif tilt == 'up':
        microbit.display.show(microbit.Image('00900:'
                                             '09990:'
                                             '99999:'
                                             '00900:'
                                             '00900'))
    elif tilt == 'down':
        microbit.display.show(microbit.Image('00900:'
                                             '00900:'
                                             '99999:'
                                             '09990:'
                                             '00900'))
    else:
        microbit.display.show(microbit.Image('90009:'
                                             '09090:'
                                             '00900:'
                                             '09090:'
                                             '90009'))

#...................
#...................

# settings
group_id=27

# setup radio receive order
radio.on()
radio.config(group=group_id)


##################### ATTENTION: TO BE DELETED #####################
### temporary code, to be deleted on final project upload
### allows to check the integrity of tilt direction readings
### comment or uncomment when needed
# while True:
#     show_tilt_on_screen()
#     microbit.sleep(50)




# loop forever (until micro:bit is switched off)
while True:
    # get view of the board
    view = get_message()

    # clear screen
    microbit.display.clear()

    # show view of the board
    if view:
        microbit.display.show(microbit.Image(view))

    # wait for button A or B to be pressed
    while not(microbit.button_a.is_pressed() or microbit.button_b.is_pressed()):
        microbit.sleep(50)

        if microbit.button_a.is_pressed():
            # send current direction
            tilt = get_tilt()
            if tilt:
                radio.send(tilt)

        elif microbit.button_b.is_pressed():
            # notify the piece should be dropped
            radio.send('drop')
