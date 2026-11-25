#this function searches for the boundry angles to interpolate
#math for rounding
import math

#function for getting shoulder calibration interpolation bounds
def bound_searcher(inter, file):
    tuned_values = {}
    print(inter, type(inter))
    #is the upper bound of interpolated value, rounded to next 10th
    hi = math.ceil(float(inter) / 10) * 10
    #lower bound of interpolated value, rounded to previous 10th
    lo = math.floor(float(inter) / 10) * 10
    #print for debugging
    print(hi, lo)
    #gets shoulder calibration values
    #creates dataframe from file
    #will change file path before upload
    with open(file) as csvfile:
        reader = csvfile
        next(reader)
        for row in reader:
            line = row.strip().split(',')
            tuned_values[line[0]] = float(line[1])
    #returns value for the high bound
    hi_bound = tuned_values.get(str(hi))
    #returns value for the low bound
    lo_bound = tuned_values.get(str(lo))
    #returns elbow bounds and their values
    return hi_bound, hi, lo_bound, lo


"""#for coding / debugging
#inputs would be from calculations block
user_input1 = input("Enter angle number for shoulder: ")
#calls shoulder calibration function
#returns the interpolation bounds and bound values
hi_S, hi_valS, lo_S, lo_valS = bound_searcher(user_input1,
                            "Shoulder_Servo_Calibration_Values.csv")
user_input2 = input("Enter angle number for elbow: ")
#calls elbow calibration function
#returns the interpolation bounds and bound values
hi_E, hi_valE, lo_E, lo_valE = bound_searcher(user_input2,
                            "Elbow_Servo_Calibrated_Values.csv")
#print statement for debugging
print(f"Shoulder hi bound:{hi_valS} = {hi_S}", type(hi_S))
print(f"Shoulder lo bound:{lo_valS} = {lo_S}", type(lo_S))
print(f"Elbow hi bound:{hi_valE} = {hi_E}", type(hi_E))
print(f"Elbow lo bound:{lo_valE} = {lo_E}", type(lo_E))"""
