#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain = Brain()

# Robot configuration code
distance_9 = Distance(Ports.PORT9)
left_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT4, GearSetting.RATIO_18_1, True)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)
motor_group_7_motor_a = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
motor_group_7_motor_b = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True)
motor_group_7 = MotorGroup(motor_group_7_motor_a, motor_group_7_motor_b)
distance_8 = Distance(Ports.PORT8)
distance_10 = Distance(Ports.PORT10)
distance_20 = Distance(Ports.PORT20)


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
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

wait(200, MSEC)
print("\033[2J")
#endregion VEXcode Generated Robot Configuration

from vex import *

# Global state control
myVariable = 0
flipbot = Event()
running = True

# Behavior Functions
def forward():
    global running
    wait(0.1, SECONDS)
    while running:
        if distance_5.is_object_detected():
            drivetrain.stop()
            wait(0.1, SECONDS)
            drivetrain.drive_for(FORWARD, 24, INCHES)
        wait(5, MSEC)

def twist():
    global running
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(200, RPM)
    while running:
        drivetrain.turn_for(RIGHT, 95, DEGREES)
        drivetrain.turn_for(LEFT, 95, DEGREES)
        wait(5, MSEC)

def turn_right():
    global running
    while running:
        if distance_20.is_object_detected():
            drivetrain.turn_for(RIGHT, 90, DEGREES)
        wait(5, MSEC)

def turn_around():
    global running
    while running:
        if distance_8.is_object_detected():
            drivetrain.turn_for(RIGHT, 180, DEGREES)
        wait(5, MSEC)

def turn_left():
    global running
    while running:
        if distance_10.is_object_detected():
            drivetrain.turn_for(LEFT, 90, DEGREES)
        wait(5, MSEC)

def flip():
    global running
    Motor_Group_7.set_max_torque(300, PERCENT)
    while running:
        if distance_5.object_distance(MM) < 300:
            Motor_Group_7.spin_for(FORWARD, 180, DEGREES)
            Motor_Group_7.spin_for(REVERSE, 180, DEGREES)
            Motor_Group_7.stop()
        wait(5, MSEC)

def line_detect_turn():
    global running
    while running:
        if line_sensor.reflectivity() < 50:
            drivetrain.turn_for(RIGHT, 180, DEGREES)
            wait(500, MSEC)  # Prevent multiple triggers
        wait(50, MSEC)

# Mode system
controller = Controller()
current_mode = "A"
button_a_prev_state = False
mode_thread = None

def mode_a():
    global ws2, ws3, ws4, ws5, ws6, ws7
    ws2 = Thread(twist)
    ws3 = Thread(turn_right)
    ws4 = Thread(turn_around)
    ws5 = Thread(turn_left)
    ws6 = Thread(flip)
    ws7 = Thread(line_detect_turn)
    forward()

def mode_b():
    brain.screen.print("Mode B active")
    while running:
        wait(100, MSEC)

def start_mode(mode):
    global mode_thread, running
    running = False
    wait(100, MSEC)
    running = True
    if mode_thread is not None:
        mode_thread.stop()
    if mode == "A":
        mode_thread = Thread(mode_a)
    elif mode == "B":
        mode_thread = Thread(mode_b)

start_mode(current_mode)

# Main loop for mode toggling
while True:
    button_a_current = controller.buttonA.pressing()
    if button_a_current and not button_a_prev_state:
        current_mode = "B" if current_mode == "A" else "A"
        brain.screen.clear_screen()
        brain.screen.print("Switched to Mode " + current_mode)
        start_mode(current_mode)
    button_a_prev_state = button_a_current
    wait(50, MSEC)
