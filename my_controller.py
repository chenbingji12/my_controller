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

motor2 = robot.getDevice('d2')
motor3 = robot.getDevice('d3')
motor4 = robot.getDevice('d4')

motor6 = robot.getDevice('d6')
motor7 = robot.getDevice('d7')
motor8 = robot.getDevice('d8')

motor10 = robot.getDevice('d10')
motor11 = robot.getDevice('d11')
motor12 = robot.getDevice('d12')

motor14 = robot.getDevice('d14')
motor15 = robot.getDevice('d15')
motor16 = robot.getDevice('d16')

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
    
    q2,q3,q4=servo_control.leg_run(time_s,1.0,0.08,0.05,0.1,0.1)
    motor2.setPosition(q2+math.radians(20))
    motor3.setPosition(q3)
    motor4.setPosition(q4)

    q6,q7,q8=servo_control.leg_run(time_s,1.0,0.08,0.05,0.1,0.1)
    motor6.setPosition(q6-math.radians(20))
    motor7.setPosition(q7)
    motor8.setPosition(q8)

    q10,q11,q12=servo_control.leg_run(time_s,1.0,0.08,0.05,0.1,0.1)
    motor10.setPosition(q10-math.radians(20))
    motor11.setPosition(q11)
    motor12.setPosition(q12)

    q14,q15,q16=servo_control.leg_run(time_s,1.0,0.08,0.05,0.1,0.1)
    motor14.setPosition(q14+math.radians(20))
    motor15.setPosition(q15)
    motor16.setPosition(q16)

# Enter here exit cleanup code.
