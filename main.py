#!/usr/bin/env pybricks-micropython
#Importing the required modules for the Lego Mindstorm to run
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font 
import threading
print("Start")

# Defines the Falling off Table function so that if the sensor overhangs on the table the program will exit otherwise it will continue the loop
def Fall_Off_Table():
    while True:
        Fallen_Off_Table = line_sensor.reflection()
        if Fallen_Off_Table == 0 :
            ev3.screen.print("Fallen off the table")
            quit()
        else:
            continue    

# Defines the colour checking variable
def colour_check(turn_amount):
    while True:
        Both_Motors.straight(x)
        colour_of_line = line_sensor.reflection()
        if colour_of_line <10 and colour_of_line != 0:
            break
        elif colour_of_line == 0:
            quit()
        else:
            continue
    Both_Motors.turn(turn_amount)

# Threading
threading.Thread(target=Fall_Off_Table).start() # Runs the Fall_Off_Table function as a thread

# Declaring Variables
x=15
Left_Motor,Right_Motor,ev3= Motor(Port.A),Motor(Port.D),EV3Brick()
Both_Motors =DriveBase(Left_Motor, Right_Motor, wheel_diameter=41.5, axle_track=104)
line_sensor = ColorSensor(Port.S2)
ev3.screen.print("Variables Declared")

# Actual Program
ev3.light.on(Color.RED)
colour_check(550)
colour_check(-450)
colour_check(-620)
colour_check(680)
colour_check(0)
wait(5000)