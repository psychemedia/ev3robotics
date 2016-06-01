# Red buttons: left motor; blue buttons: right motor.

from time import sleep
from ev3dev.auto import *

# Connect large motors on output ports A and B
MOTOR_LEFT = LargeMotor(OUTPUT_A)
MOTOR_RIGHT = LargeMotor(OUTPUT_B)

# Connect remote control
rc = RemoteControl()

# Define button handler
button = Button()

# Assign event handler to each of the remote buttons
rc.on_red_up = lambda x: MOTOR_LEFT.run_forever(duty_cycle_sp=75) if x else MOTOR_LEFT.stop()
rc.on_red_down = lambda x: MOTOR_LEFT.run_forever(duty_cycle_sp=-75) if x else MOTOR_LEFT.stop()
rc.on_blue_up = lambda x: MOTOR_RIGHT.run_forever(duty_cycle_sp=75) if x else MOTOR_RIGHT.stop()
rc.on_blue_down = lambda x: MOTOR_RIGHT.run_forever(duty_cycle_sp=-75) if x else MOTOR_RIGHT.stop()

# Enter event processing loop
while not button.any():
    rc.process()
    sleep(0.01)

MOTOR_LEFT.stop()
MOTOR_RIGHT.stop()