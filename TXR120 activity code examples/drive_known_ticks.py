from ev3dev.auto import *
from time import sleep

FORWARDS=1
BACKWARDS = FORWARDS * -1

#Configure motors
LEFT_MOTOR = LargeMotor(OUTPUT_A)
RIGHT_MOTOR = LargeMotor(OUTPUT_B)

def motors_on(direction=FORWARDS, duty_cycle_sp=50):
    #Turn motors on
    LEFT_MOTOR.run_forever(duty_cycle_sp=direction * duty_cycle_sp)
    RIGHT_MOTOR.run_forever(duty_cycle_sp=direction * duty_cycle_sp)

def motors_off(stop_command='brake'):
    ''' brake | hold | coast '''
    #Set stop_command
    LEFT_MOTOR.stop_command = stop_command
    RIGHT_MOTOR.stop_command = stop_command

    #Turn motors off
    LEFT_MOTOR.stop()
    RIGHT_MOTOR.stop()

# Find the current position as a reference position
current_pos_left = LEFT_MOTOR.position

#Set the distance
TICKS = 360

motors_on()

while LEFT_MOTOR.position < current_pos_left + TICKS:
    # We haven't reached the positive, going forward position yet, so carry on
    sleep(0.01)

motors_off()

#What calculation would you have to do to drive BACKWARDS a desired number of TICKS?