import math
tuned_values = {}
inter = 21.2
hi = math.ceil(float(inter) / 10) * 10
lo = math.floor(float(inter) / 10) * 10
with open('Shoulder_Servo_Recalibrated_Values.csv') as csvfile:
    #reader = csv.DictReader(csvfile, fieldnames=['programmed', 'call'])
    reader = csvfile
    next(reader)
    for row in reader:
        line = row.strip().split(',')
        tuned_values[line[0]] = float(line[1])
for key, value in tuned_values.items():
    print(key, value)
print(hi, tuned_values.get(str(hi)))
print(lo, tuned_values.get(str(lo)))
