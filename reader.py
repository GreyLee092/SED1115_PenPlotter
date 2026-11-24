tuned_values = {}
with open('Shoulder_Servo_Recalibrated_Values.csv') as csvfile:
    #reader = csv.DictReader(csvfile, fieldnames=['programmed', 'call'])
    reader = csvfile
    next(reader)
    for row in reader:
        line = row.strip().split(',')
        print(line)
        tuned_values[line[0]] = float(line[1])
for key, value in tuned_values.items():
    print(key, value)
print(tuned_values.get('140'))