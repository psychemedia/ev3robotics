# # TouchSensor Bumper
# In this activity, you will learn how to monitor the EV3 robot's touch sensor

# Attach the touch sensor to the brick and use the `Device Browser` to find the sensor.
# Select *Watch values* to monitor the values of the sensor
# Record the value of the sensor when the touch sensor is pressed and not pressed.
# How would you use the sensor value to detect when the robot has bumped into something?

from ev3dev.auto import *
from time import sleep

#Configure motors
LEFT_MOTOR = LargeMotor(OUTPUT_A)
RIGHT_MOTOR = LargeMotor(OUTPUT_B)

def start_motors(duty_cycle_sp=50):
    LEFT_MOTOR.run_forever(duty_cycle_sp=duty_cycle_sp)
    RIGHT_MOTOR.run_forever(duty_cycle_sp=duty_cycle_sp)

def turn_motors(duty_cycle_sp=50, direction=1):
    LEFT_MOTOR.run_forever(duty_cycle_sp=direction * duty_cycle_sp)
    RIGHT_MOTOR.run_forever(duty_cycle_sp=-1 * direction * duty_cycle_sp)


def stop_motors(stop_command='brake'):
    ''' brake | coast | hold '''
    LEFT_MOTOR.stop(stop_command=stop_command)
    RIGHT_MOTOR.stop(stop_command=stop_command)

buttons=Button()

ts = TouchSensor()

#Continue driving until you see the black line and then stop
threshold = 50

#Start driving
start_motors()

while not buttons.any():
    if ts.value():
        #We've bumped, so reverse for a bit
        start_motors(duty_cycle_sp=-50)
        sleep(2)
        turn_motors()
        sleep(1)
        start_motors(duty_cycle_sp=50)

stop_motors()