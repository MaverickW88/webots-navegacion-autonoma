# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 21:31:47 2020

@author: Humberto Guzman G
"""
"""P1cont controller."""

# First we import the necesary libraries
from controller import Robot
from controller import Motor
from controller import Keyboard
from controller import PositionSensor
# Then we create the Robot instance.
robot = Robot()
keyboard = Keyboard()
# Next we get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
# We assign the timestep to the keyboard function
keyboard.enable(timestep)
# Next we initialize the motors



wheels = []
wheelsNames = ['m1', 'm2']
for name in wheelsNames:
    wheels.append(robot.getMotor(name))
# And the position sensors
ds = []
dsNames = ['sens1', 'sens2']
for i in range(2):
    ds.append(robot.getPositionSensor(dsNames[i]))
    ds[i].enable(timestep)
# We assign PID controller for motors
p = 10
i = 1
d = 1

# Then we initialize speed and position variables
error = 0
previous_error = 0
errorA = 0
error_integral = 0
error_derivativo = 0
speed = 0
posr = 0.0
posl = 0.0
a = 0.0
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    map=[1,2,3,4,5,6,7,8,9,]
    
    
    
    
    # First we get the pressed key
    key = keyboard.getKey()
    # We determine the movement depending on the key
    if key == Keyboard.DOWN:
        posl = posl + .10
        posr = posr + .10
    elif key == Keyboard.UP:
        posl = posl - .10
        posr = posr - .10
    elif key == Keyboard.LEFT:
        posl = posl + .20
        posr = posr - .10
    elif key == Keyboard.RIGHT:
        posl = posl - .10
        posr = posr + .10
    # Next we use a PID controller to determine velocity
    previous_error = error;
    error = wheels[0].getTargetPosition()- ds[0].getValue()
    error_integral += error * timestep
    error_derivative = (previous_error - error) / timestep
    speed = p * error + d * error_derivative + i * error_integral ;
    if speed < 0:
        speed = -1.0 * speed
    if speed >= 10:
        speed = 10
    # We assign the movement to the motors
    wheels[1].setPosition(posr)
    wheels[1].setVelocity(speed)
    wheels[0].setPosition(posl)
    wheels[0].setVelocity(speed)
    pass
