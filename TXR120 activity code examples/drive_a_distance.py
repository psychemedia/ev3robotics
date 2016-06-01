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

#The basic tyre supplied with the Lego EV3 has a diameter of 56mm (it's written on the tyre).
#It can also be calcuated from the radius, or diameter of the tyre etc etc
#So 1 revolution moves the robot 56mm = 56mm / 1000mm per m = 0.056m

#Distance per tick = circumference / ticks per revolution
#Distance per tick= 1 / distance per tick = 1 / ( (pi * 56 / 1000) / 360) = 360 / (pi * 56 / 1000)
#TICKS_PER_M = (360 * 1000) / (pi * 56) # ~2046
#Define a function to convert a distance into a number of ticks

from math import pi
#This may require a bit of calibration - the calculation gives us a first guess
TICKS_PER_M = (360 * 1000) / (pi * 56)

def ticks_for_distance(distance_in_meters):
    #Calculate how many ticks correspond to the specified distance in meters
    ticks= TICKS_PER_M * distance_in_meters
    return ticks

#Set the distance
TICKS = ticks_for_distance(0.1)

# Find the current position as a reference position
current_pos_left = LEFT_MOTOR.position

motors_on()


while LEFT_MOTOR.position < current_pos_left + TICKS:
    # We haven't reached the positive, going forward position yet, so carry on
    sleep(0.01)

motors_off()