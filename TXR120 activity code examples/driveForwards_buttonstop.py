from ev3dev.auto import *
from time import sleep

#Configure motors
LEFT_MOTOR = LargeMotor(OUTPUT_A)
RIGHT_MOTOR = LargeMotor(OUTPUT_B)

#Get a handle for the buttons EV3 brick
buttons=Button()


#Turn motors on
LEFT_MOTOR.run_forever(duty_cycle_sp=75)
RIGHT_MOTOR.run_forever(duty_cycle_sp=75)

# Sit twiddling our thumbs going round the while loop while no buttons are pressed
while not buttons.any():
    sleep(0.01)
    #The sleep gives the robot a chance to see the button press

#Turn motors off
LEFT_MOTOR.stop()
RIGHT_MOTOR.stop()
