# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:09:45 2020

@author: Humberto Guzman G
"""


"""Controller_Practice1 controller."""

from controller import Robot
from controller import Motor
from controller import Keyboard

# create the Robot instance.
robot = Robot()

# initialize motors
wheels = []
wheelsNames = ['left_w', 'right_w']
for name in wheelsNames:
    wheels.append(robot.getMotor(name))

# implemet PID control
P = 10
I = 1
D = 1
left_w.setControlPID(P,I,D)
right_w.setControlPID(P,I,D)

# initialize keyboard
kboard = Keyboard();

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# variable
posr = 0.0;
posl = 0.0;

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # get the pressed key
    kboard.enable(timestep)
    key = kboard.getKey()
    left_w.setVelocity(5.0);
    right_w.setVelocity(5.0);
    # move robot
    posr = 0.0
    posl = 0.0
    if key == Keyboard.LEFT:
       posr = posr + 6.28
       posl = posl - 6.28
    elif key == Keyboard.RIGHT:
        posr = posr - 6.28
        posl = posl + 6.28
    elif key == Keyboard.UP:
        posr = posr - 6.28
        posl = posl + 6.28
    elif key == Keyboard.DOWN:
        posr = posr - 6.28
        posl = posl + 6.28
    pass

pass
# Enter here exit cleanup code.7