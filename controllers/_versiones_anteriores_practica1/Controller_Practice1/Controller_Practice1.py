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
kboard = Keyboard()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # get the pressed key
    kboard.enable(timestep)
    key = kboard.getKey()
    left_w.setVelocity(5.0);
    right_w.setVelocity(5.0);
    # move robot
    switch(key) {
    	case Keyboard.LEFT: 
    		left_w.setPosition(pos - 6.28)
    		right_w.setPosition(pos + 6.28)
    	case Keyboard.RIGHT:
    		left_w.setPosition(pos + 6.28)
    		right_w.setPosition(pos - 6.28)
    	case Keyboard.UP:
    		left_w.setPosition(pos + 6.28)
    		right_w.setPosition(pos + 6.28)
    	case Keyboard.DOWN:
    		left_w.setPosition(pos - 6.28)
    		right_w.setPosition(pos - 6.28)
    }

    pass