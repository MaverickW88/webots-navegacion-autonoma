"""p2_controller"""
# First we import the necesary libraries
from controller import Robot
from controller import Motor
from controller import Keyboard
from controller import PositionSensor
# Definition of robot
robot = Robot()
# Definition of timestep
timestep = int(robot.getBasicTimeStep())
# Definition of keyboard
keyboard = Keyboard()
keyboard.enable(timestep)
# Definition of ir sensors
ir = []
irNames = ['ir1', 'ir2', 'ir3']
for i in range(3):
    ir.append(robot.getDistanceSensor(irNames[i]))
    ir[i].enable(timestep)
# Definition of motors
m = []
mNames = ['m1', 'm2']
for name in mNames:
    m.append(robot.getMotor(name))
# Definition of position sensors
ps = []
psNames = ['sens1', 'sens2']
for i in range(2):
    ps.append(robot.getPositionSensor(psNames[i]))
    ps[i].enable(timestep)
# PID variables
p = 10
i = 10
d = 5
error = 0
previous_error = 0
errorA = 0
error_integral = 0
error_derivativo = 0
speed = 0
posr = 0.0
posl = 0.0
a = 0.0
# Controller main
while robot.step(timestep) != -1:
    # First we get the pressed key
    # We determine the movement depending on the key
    if ir[0].getValue() > 200:
        while ir[1].getValue() < 200:
            posl = posl - 0.25
            posr = posr + 0.25
            print("delante")
    elif ir[2].getValue() > 200:
         while ir[1].getValue() < 200:
            posl = posl + 0.25
            posr = posr - 0.25
            print("izquierda")
    else:
        posl = posl - 0.10
        posr = posr - 0.10
        print("derecha")   
    # Next we use a PID controller to determine velocity
    previous_error = error;
    error = m[0].getTargetPosition()- ps[0].getValue()
    error_integral += error * timestep
    error_derivative = (previous_error - error) / timestep
    speed = p * error + d * error_derivative + i * error_integral ;
    if speed < 0:
        speed = -1.0 * speed
    if speed >= 10:
        speed = 10
    # We assign the movement to the motors
    m[1].setPosition(posr)
    m[1].setVelocity(speed)
    m[0].setPosition(posl)
    m[0].setVelocity(speed)
    pass