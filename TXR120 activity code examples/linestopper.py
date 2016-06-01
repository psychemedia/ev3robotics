# # LineStopper Challenge
# In this activity, you will learn how to monitor one of the EV3 robot's sensors in order to detect a black line
# Your robot should drive forwards until it sees the black line and then stop

# Attach the colour sensor to the brick and use the `Device Browser` to find the sensor.
# Select *Watch values* to monitor the values of the sensor
# Record the value of the sensor over white and black backgrounds.
# How would you use the sensor values to distinguish between black and white backgrounds?

from ev3dev.auto import *
from time import sleep


#Configure motors
LEFT_MOTOR = LargeMotor(OUTPUT_A)
RIGHT_MOTOR = LargeMotor(OUTPUT_B)


def stop_motors(stop_command='brake'):
    ''' brake | coast | hold '''
    LEFT_MOTOR.stop(stop_command=stop_command)
    RIGHT_MOTOR.stop(stop_command=stop_command)

cs = ColorSensor()


#set the mode
cs.mode='COL-REFLECT'

#Continue driving until you see the black line and then stop
threshold = 50

#Start driving
LEFT_MOTOR.run_forever(duty_cycle_sp=25)
RIGHT_MOTOR.run_forever(duty_cycle_sp=25)



while cs.value()>threshold:
    sleep(0.01)

stop_motors()

