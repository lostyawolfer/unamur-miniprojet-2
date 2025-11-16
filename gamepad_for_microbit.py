import microbit
import radio

def get_message():
    message=None
    while message==None:
        microbit.sleep(250)
        message=radio.receive()
    return message

def get_tilt() -> str | None:
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    if abs(x) > abs(y):
        return 'right' if y > 0 else 'left'
    elif abs(y) > abs(x):
        return 'down' if y > 0 else 'up'
    else:
        return None
 
group_id=27
radio.on()
radio.config(group=group_id)

while True:
    view = get_message()
    microbit.display.clear()
    if view:
        microbit.display.show(microbit.Image(view))
    while not(microbit.button_a.is_pressed() or microbit.button_b.is_pressed()):
        microbit.sleep(50)
        if microbit.button_a.is_pressed():
            tilt = get_tilt()
            if tilt:
                radio.send(tilt)
        elif microbit.button_b.is_pressed():
            radio.send('drop')
