from machine import Pin,PWM
from Servo_Angle_Translator import translate

#Defines Shoulder servo as pin 0
servo_S = PWM(Pin(0))
#Shoulder servo has a frequency of 50hz
servo_S.freq(50)
#Defines Elbow servo as pin 1
servo_E = PWM(Pin(1))
#Elbow servo has a frequency of 50hz
servo_E.freq(50)
#Defines Wrist servo as pin 2
servo_W = PWM(Pin(2))
#Wrist servo has a frequency of 50hz
servo_W.freq(50)

#shoulder servo at 0˚ is 10˚ counter-clockwise from vertical axis
#inputted value to match 10˚ is 17˚
#shoulder servo range is from 10˚ to 140˚
#we need to find value to subtract from inputted value to calibrate it

#function runs through angles in 10˚ increments to measure difference
#of inputs and outputs
def shoulder_calibration():
    #straightens elbow servo
    servo_E.duty_u16(translate(150))
    #puts pen in down position
    servo_W.duty_u16(translate(30))
    #waiting for input prompt
    input("Start Shoulder Calibration")
    #minimum angle is 10˚ and maximum is 140˚
    for i in range(10, 150, 10):
        #programmed angle is actuated and printed
        servo_S.duty_u16(translate(i))
        print(f"servo is at {i}˚")
        input()

#function runs through angles in 10˚ increments to measure difference
#of inputs and outputs
def elbow_calibration():
    #sets shoulder to a constant angle
    servo_S.duty_u16(translate(10))
    #sets pen in down position
    servo_W.duty_u16(translate(30))
    #waiting for input prompt
    input("Start Elbow Calibration")
    #minimum angle is 10˚ and maximum is 180˚
    for i in range(10, 190, 10):
        #programmed angle is actuated and printed
        servo_E.duty_u16(translate(i))
        print(f"servo is at {i}˚")
        input()

#function to interpolate angle
def servo_interpolation(angle):
    #defines angle as float value
    angle = float(angle)
    #x values
    #rounds up to 10s decimal
    upper_bound = round(angle, -1)
    #rounded down 10s decimal
    lower_bound = upper_bound-10
    #y values
    #the values we measured as calibrations
    upper_bound_real = int(input(f"enter measured angle for {upper_bound}˚: "))
    lower_bound_real = int(input(f"enter measured angle for {lower_bound}˚: "))
    #linear interpolation
    #finds slope
    slope = (upper_bound_real - lower_bound_real) / 10
    #y intercept
    y_intercept = upper_bound_real - (slope * upper_bound)
    #returns y value of inputted x coordinate
    return slope * angle + y_intercept

#could use some reform
input()
while True:
    #collects input
    us_inp = input("Enter: "
                   "'e' for elbow calibration"
                   "'s' for shoulder calibration"
                   "'run' for calibration testing"
                   "'stop' to end program")
    #performs elbow servo calibration
    if us_inp == 'e':
        elbow_calibration()
    #performs shoulder servo calibration
    elif us_inp == 's':
        shoulder_calibration()
    #performs value check of 'x' degree
    elif us_inp == 'run':
        servo_S.duty_u16(translate(10))
        degree = input("Enter a degree: ")
        #degree = servo_calibration(degree)
        servo_E.duty_u16(translate(float(degree)))
    elif us_inp == 'stop':
        print("end program")
        break
    else:
        print("invalid input")