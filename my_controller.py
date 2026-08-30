"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import servo_control
import math


# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

time_s=0.0

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

motor1 = robot.getDevice('d1')
motor5 = robot.getDevice('d5')
motor6 = robot.getDevice('d6')
motor7 = robot.getDevice('d7')

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    time_s=time_s+timestep/1000.0

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    
    pos=math.radians(120)

    motor1.setPosition(pos*math.sin(time_s))

    print(pos*math.sin(time_s),time_s)

# Enter here exit cleanup code.
