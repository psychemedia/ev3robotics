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


def drive_N_ticks(N=360, dirSpeed=50):

    if dirSpeed < 0:
        direction=BACKWARDS
        dirSpeed = abs(dirSpeed)
    else:
        direction=FORWARDS

    # Ensure that we have a positive number of ticks by taking the absolute value of the ticks
    N = abs(N)

    # Find the current position as a reference position
    current_pos_left = LEFT_MOTOR.position

    # Set the motor speed and direction
    motors_on(direction,dirSpeed)

    if direction == FORWARDS:
        # If the direction is positive, go forwards until we reach the target position
        while LEFT_MOTOR.position < current_pos_left + N:
            # We haven't reached the positive, going forward position yet, so carry on
            sleep(0.01)
    else:
        # If the direction is negative, go backwards until we reach the target position
        while LEFT_MOTOR.position > current_pos_left - N:
            # We haven't reached the negative, going backward position yet, so carry on
            sleep(0.01)

    motors_off('brake')

from math import pi
TICKS_PER_M = (360 * 1000) / (pi * 56)

def ticks_for_distance(distance_in_meters):
    #Calculate how many ticks correspond to the specified distance in meters
    ticks= TICKS_PER_M * distance_in_meters
    return ticks

def drive_for_M_meters(distance_in_meters=0.25,dirSpeed=50):
    drive_N_ticks(ticks_for_distance(distance_in_meters),dirSpeed)

drive_for_M_meters(0.30)