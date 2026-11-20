import math

#imports function to read calibrated servo angle table
#from Calibrated_Value_Finder import bound_searcher
#translate function to turn degrees into duty values
from Servo_Angle_Translator import translate

#function to initiate calculations
def calculation(x_coor, y_coor):
    #calls function to determine the vector length
    vector = hypotenuse_length(x_coor, y_coor)
    #calls function to determine the inner arm angles from the vector
    print(vector, type(vector))
    angle_shoulder, angle_elbow = angles((vector/2))
    #returns angles in degrees
    return angle_shoulder, angle_elbow

#function to get the hypotenuse of the armature triangle
def hypotenuse_length(x, y):
    #shoulder root x position
    origin_x = -50
    #shoulder root y position
    origin_y = 139.5
    #returns length of vector
    return math.sqrt(math.pow(x - origin_x, 2) + math.pow(y - origin_y, 2))

#function to get the inner angles of the armature triangle
def angles(adjacent):
    #length of the arm is known
    hypotenuse = 15*180
    #arcsine to find the angle using the hypotenuse and adjacent lengths
    angle_a = math.degrees(math.acos(adjacent / hypotenuse))
    #180˚ - other angles to get the unknown angle
    angle_b = 180 - (2 * angle_a)
    #returns angles
    return angle_a, angle_b

#interpolation of values from table
def servo_interpolation(angle, b, c, d, e):
    #defines variables, target is the bound in increments of 10
    upper_bound_target = b
    #real is the value measured during calibration
    upper_bound_real =  c
    lower_bound_target = d
    lower_bound_real =  e
    #finds slope
    slope = ((upper_bound_real - lower_bound_real) /
             (upper_bound_target - lower_bound_target))
    #y intercept
    y_intercept = upper_bound_real - (slope * upper_bound_target)
    #returns calibration value for inputted angle
    return slope * angle + y_intercept

#main function, called by Potentiometer_Inputs
def main(x_pos, y_pos):
    #calls function to calculate servo angles
    shoulder_angle, elbow_angle = calculation(x_pos, y_pos)
    """
    #calls function to read csv getting calibration values for the shoulder servo
    hi_bound, hi_value, lo_bound, lo_value = bound_searcher(shoulder_angle,
                                                "Shoulder_Servo_Calibration_Values.csv")
    #calls function to read csv getting calibration values for the elbow servo
    top_bound, top_value, bot_bound, bot_value = bound_searcher(elbow_angle,
                                                "Elbow_Servo_Calibrated_Values.csv")
    #runs interpolation function for shoulder angle then translates shoulder servo
    shoulder_motion = translate(servo_interpolation(shoulder_angle, hi_bound, hi_value, lo_bound, lo_value))
    #runs interpolation function for elbow angle then translates elbow servo
    elbow_motion = translate(servo_interpolation(elbow_angle, top_bound, top_value, bot_bound, bot_value))
    """
    shoulder_motion = translate(shoulder_angle)
    elbow_motion = translate(elbow_angle)
    return shoulder_motion, elbow_motion



