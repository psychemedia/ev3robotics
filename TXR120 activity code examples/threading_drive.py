from ev3dev.auto import *
from threading import Thread

#test
done=False
def emergency_stop():
    global done
    buttons = Button()
    while not buttons.any():
        pass
    motors_off()
    done=True


LEFT_MOTOR = LargeMotor(OUTPUT_B)
RIGHT_MOTOR = LargeMotor(OUTPUT_C)

def motors_on(direction=1, duty_cycle_sp=50):
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

stopper=Thread(target=emergency_stop)
stopper.start()

motors_on()

while not done:
    pass