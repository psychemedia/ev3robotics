from ev3dev.auto import *
from time import sleep

#Configure motors
LEFT_MOTOR = LargeMotor(OUTPUT_A)
RIGHT_MOTOR = LargeMotor(OUTPUT_B)

#Turn motors on
LEFT_MOTOR.run_forever(duty_cycle_sp=75)
RIGHT_MOTOR.run_forever(duty_cycle_sp=75)

#Drive for two seconds
sleep(2)


#Note: experiment with stop() commands via eg: stop | hold | coast
#LEFT_MOTOR.stop_command = 'brake'
#RIGHT_MOTOR.stop_command = 'brake'

#Turn motors off
LEFT_MOTOR.stop()
RIGHT_MOTOR.stop()

