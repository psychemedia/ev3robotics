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


#Drive forwards for two seconds
motors_on(FORWARDS)
sleep(2)


#Turn for 2s one way
motors_turn(CW)
sleep(2)

#Turn for 2s the other way
motors_turn(CCW)
sleep(2)

#Turn motors off
motors_off()

