from ev3dev.auto import *
from time import sleep

FORWARDS=1
BACKWARDS = FORWARDS * -1

CW = 1
CCW = -1

#Configure motors
LEFT_MOTOR = LargeMotor(OUTPUT_A)
RIGHT_MOTOR = LargeMotor(OUTPUT_B)

def motors_on(direction=FORWARDS, duty_cycle_sp=50):
    #Turn motors on
    LEFT_MOTOR.run_forever(duty_cycle_sp=direction * duty_cycle_sp)
    RIGHT_MOTOR.run_forever(duty_cycle_sp=direction * duty_cycle_sp)

def motors_turn(turndir=CW, duty_cycle_sp=50):
    #Turn motors on
    LEFT_MOTOR.run_forever(duty_cycle_sp=turndir * duty_cycle_sp)
    RIGHT_MOTOR.run_forever(duty_cycle_sp= -1 * turndir * duty_cycle_sp)

def motors_off(stop_command='brake'):
    ''' brake | hold | coast '''
    #Set stop_command
    LEFT_MOTOR.stop_command = stop_command
    RIGHT_MOTOR.stop_command = stop_command

    #Turn motors on
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
            pass
    else:
        # If the direction is negative, go backwards until we reach the target position
        while LEFT_MOTOR.position > current_pos_left - N:
            # We haven't reached the negative, going backward position yet, so carry on
            pass

    motors_off('brake')

#We can pretty much reuse the drive_N_ticks function - just turn and set the turn direction flags
def turn_N_ticks(N=360, dirSpeed=50):

    if dirSpeed < 0:
        direction=CW
        dirSpeed = abs(dirSpeed)
    else:
        direction=CCW

    # Ensure that we have a positive number of ticks by taking the absolute value of the ticks
    N = abs(N)

    # Find the current position as a reference position
    current_pos_left = LEFT_MOTOR.position

    # Set the motor speed and direction
    motors_turn(direction,dirSpeed)

    if direction == CW:
        # If the direction is positive, go forwards until we reach the target position
        while LEFT_MOTOR.position < current_pos_left + N:
            # We haven't reached the positive, going forward position yet, so carry on
            pass
    else:
        # If the direction is negative, go backwards until we reach the target position
        while LEFT_MOTOR.position > current_pos_left - N:
            # We haven't reached the negative, going backward position yet, so carry on
            pass

    motors_off('brake')

from math import pi
TICKS_PER_M = (360 * 1000) / (pi * 56)

def ticks_for_distance(distance_in_meters):
    #Calculate how many ticks correspond to the specified distance in meters
    ticks= TICKS_PER_M * distance_in_meters
    return ticks

def drive_for_M_meters(distance_in_meters=0.25,dirSpeed=50):
    drive_N_ticks(ticks_for_distance(distance_in_meters),dirSpeed)

TRACK=120
DISTANCE_PER_DEGREE = (pi * TRACK / 1000) / 360

def ticks_for_angle(angle):
    #Calculate how many ticks correspond to the specified distance in meters
    distance = angle * DISTANCE_PER_DEGREE
    ticks = ticks_for_distance(distance)
    return ticks

def turn_for_D_degrees(angle=360, dirSpeed=50):
    turn_N_ticks( ticks_for_angle(angle), dirSpeed)