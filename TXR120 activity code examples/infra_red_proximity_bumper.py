#Program to avoid collisions based on infra-red proximity sensor state
from ev3dev.auto import *
from time import sleep
import random
from myfunctions import *

ir=InfraredSensor()

ir.mode = 'IR-PROX'

btn = Button()


motors_on(FORWARDS,60)

# Run the robot until a button is pressed.
while not btn.any():

    # Infrared sensor in proximity mode will measure distance to the closest
    # object in front of it.
    distance = ir.value()

    if distance > 60:
        # Path is clear, run at full speed.
        dc = 60
    elif distance >20:
        # Obstacle ahead, slow down.
        dc = 20
    else:
        motors_on(BACKWARDS,50)
        while ir.value() < 60:
            sleep(0.01)
        direction=random.choice([1, -1])
        angle=random.randint(10,150)
        turn_for_D_degrees(angle,direction*50)

    motors_on(FORWARDS, dc)
    sleep(0.1)

motors_off()

