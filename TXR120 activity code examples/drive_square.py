#If we build up the myfunctions.py file as we go along
#students can build directly on what they've already done

from myfunctions import *

side=0.2
angle=90

for i in range(4):
    drive_for_M_meters(side)
    turn_for_D_degrees(angle)

motors_off()