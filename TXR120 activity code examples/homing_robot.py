#Program to move to beacon
from ev3dev.auto import *
from time import sleep
import random
from myfunctions import *


#http://www.ev3dev.org/docs/sensors/lego-ev3-infrared-sensor/
ir=InfraredSensor()
ir.mode='IR-SEEK'

def ir_beacon_distDir(channel=1):
    #heading is a percentage(?)
    heading= ir.value(2*(channel-1))
    dist= ir.value(2*(channel-1)+1)
    #"Lost" code is (0, 100)
    return heading,abs(dist)

buttons=Button()

def sgn(x):
    return -1 if x<0 else 1

motors_on(FORWARDS,50)
while not buttons.any():
    heading,dist=ir_beacon_distDir()
    #if we're struggling, do some seeking...
    if heading==0 and dist==100:
        turn_for_D_degrees(random.randint(0,90),random.choice([-1,1])*50)

    heading, dist = ir_beacon_distDir()
    while abs(heading) >3 and not buttons.any():
        motors_turn(sgn(heading),15)
        heading, dist = ir_beacon_distDir()
        sleep(0.01)

    heading, dist = ir_beacon_distDir()
    if dist>100:
        speed=100
    elif dist>40:
        speed = 50
    elif dist>20:
        speed=20
    elif dist<=20:
        break

    motors_on(FORWARDS,speed)
    sleep(0.01)

motors_off()