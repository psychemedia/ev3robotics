from ev3dev.auto import *
from time import sleep
import random
from myfunctions import *

gs=GyroSensor()

#Calibrate the sensor
gs.mode = 'GYRO-CAL'
#Now go in to angular mode
gs.mode='GYRO-ANG'

#If we're within ish degrees that's close enough
ish=2

def gyro_turn_till_relative(bearing):
    #What heading does the gyro currently give, in degrees?
    current_heading=gs.value() % 360
    #The target heading is the current heading plus the desired bearing
    target_heading=(360+current_heading+bearing) % 360
    #Keep turning while the current heading is more than ish degrees from the target heading
    #Should really optimise the turn so we turn the shortest angle
    while abs(( gs.value() % 360)-target_heading) >ish:
        if gs.value() % 360 -target_heading <0:
            motors_turn(CW,25)
        else:
            motors_turn(CCW, 25)
    motors_off()

side=0.2
angle=90

for i in range(4):
    drive_for_M_meters(side)
    gyro_turn_till_relative(angle)

motors_off()