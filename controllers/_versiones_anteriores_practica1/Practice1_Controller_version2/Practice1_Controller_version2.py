"""Controller_Practice1 controller."""

from controller import Robot
from controller import Motor
from controller import Keyboard

# create the Robot instance.
robot = Robot()

# initialize motors
motor1 = robot.getMotor("left_w")
motor2 = robot.getMotor("rigth_w")

# implemet PID control
P = 10
I = 1
D = 1
motor1.setControlPID(P,I,D)
motor2.setControlPID(P,I,D)

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
    motor1.setVelocity(5.0);
    motor2.setVelocity(5.0);
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
    
    motor1.setPosition(posl);
    motor2.setPosition(posr);
pass
# Enter here exit cleanup code.