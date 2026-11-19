from machine import Pin,PWM, ADC
import time
from Servo_Angle_Translator import translate
from send_compensated_angle import main

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

#switch to raise/lower pen
switch = Pin(12, Pin.IN, Pin.PULL_DOWN)
#iterable to register button presses for toggling
n = 0

#Left potentiometer controls X axis
adcX = ADC(Pin(27))
#Right potentiometer controls Y axis
adcY = ADC(Pin(26))

#range of potentiometer, will vary between boards
potentiometer_range = 65535 - 160
#creates integer step value for virtual grid
#denominator is the number of steps desired
potentiometer_step = potentiometer_range / 180

#variable that controls how similar results are
alpha = 0.85

#lowpass filter
def lowpass(real, post):
    return alpha * post + (1 - alpha) * real

#starts program by defining variables to compare against
value_X_previous = round((adcX.read_u16() / potentiometer_step), 2)
value_Y_previous = round((adcY.read_u16() / potentiometer_step), 2)

#keeps program running
while True:
    #saves the position of X potentiometer at defined step
    #is rounded
    value_X = round((adcX.read_u16() / potentiometer_step), 2)
    #sets a lowpass band to keep values below
    X_lo_band = lowpass(value_X, value_X_previous)
    #saves the position of Y potentiometer at defined step
    #is rounded
    value_Y = round((adcY.read_u16() / potentiometer_step), 2)
    # sets a lowpass band to keep values below
    Y_lo_band = lowpass(value_Y, value_Y_previous)
    #button toggle to raise/lower pen
    if switch.value() == 1:
        #waits for button bounce to dampen
        time.sleep_ms(100)
        #if button has been pressed and then let go
        if switch.value() == 0:
            #counts iterable
            n+=1
    #if iterable is modulus 2, it can turn on
    if n % 2 == 0:
        #lower wrist servo to 30˚
        servo_W.duty_u16(translate(30))
    else:
        #raise wrist servo to 12.5˚, prevents stalling
        servo_W.duty_u16(translate(12.5))
    #if X and Y is under their respective bands
    if value_X <= X_lo_band and value_Y <= Y_lo_band:
        #runs inverse kinematics
        main(value_X, value_Y)
    #saves previous values for next loop
    value_X_previous = value_X
    value_Y_previous = value_Y




