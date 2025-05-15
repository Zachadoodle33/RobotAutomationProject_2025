#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
distance_9 = Distance(Ports.PORT9)
distance_8 = Distance(Ports.PORT8)
distance_10 = Distance(Ports.PORT10)
distance_20 = Distance(Ports.PORT20)
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
motor_group_7_motor_a = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
motor_group_7_motor_b = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
motor_group_7 = MotorGroup(motor_group_7_motor_a, motor_group_7_motor_b)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
myVariable = 0
message1 = Event()

def forward():
    global myVariable, message1
    wait(0.1, SECONDS)
    while True:
        if distance_9.is_object_detected():
            drivetrain.stop()
            wait(0.1, SECONDS)
            drivetrain.drive_for(FORWARD, 24, INCHES)
        wait(5, MSEC)
    # front sensor

def twist():
    global myVariable, message1
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(150, RPM)
    while True:
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        wait(5, MSEC)
    #

def turn_right():
    global myVariable, message1
    while True:
        if distance_20.is_object_detected():
            drivetrain.turn_for(RIGHT, 90, DEGREES)
        wait(5, MSEC)
    # right sensor

def turn_around():
    global myVariable, message1
    while True:
        if distance_8.is_object_detected():
            drivetrain.turn_for(RIGHT, 180, DEGREES)
        wait(5, MSEC)
    # back sensor

def turn_left():
    global myVariable, message1
    while True:
        if distance_10.is_object_detected():
            drivetrain.turn_for(LEFT, 90, DEGREES)
        wait(5, MSEC)
    # left sensor


myVariable = 0
flipbot = Event()

def flip():
    global myVariable, flipbot
    motor_group_7.set_max_torque(300, PERCENT)
    while True:
        if distance_9.object_distance(MM) < 300:
            motor_group_7.spin_for(FORWARD, 180, DEGREES)
            motor_group_7.spin_for(REVERSE, 180, DEGREES)
            motor_group_7.stop()
        wait(5, MSEC)



ws2 = Thread( twist )
ws3 = Thread( turn_right )
ws4 = Thread( turn_around )
ws5 = Thread( turn_left )
ws6 = Thread( flip )
forward()
