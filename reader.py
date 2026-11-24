import csv as csv
tuned_values = {}
with open('Shoulder_Servo_Recalibrated_Values.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['programmed', 'call'])
    next(reader)
    for row in reader:
        tuned_values[row['programmed']] = row['call']
for key, value in tuned_values.items():
    print(key, value)
print(tuned_values.get('10'))