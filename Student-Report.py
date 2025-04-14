report = []
while True:
    name = str(input('Name: '))
    grade1 = int(input('Grade 1: '))
    grade2 = int(input('Grade 2: '))
    average = (grade1 + grade2) / 2
    report.append([name, [grade1, grade2], average])
    
    cont = str(input('Do you want to continue? [Y/N] '))
    if cont.lower() == 'n':
        break

print('-=' * 30)
print(f'{"No":>4} {"Name":>10} {"Average":>14}')
print('-' * 30)
for i, student in enumerate(report):
    print(f'{i:>4} {student[0]:>10} {student[2]:>14.1f}')
print('-' * 30)

while True:
    idx = int(input('Show grades for which student? [999 to stop] '))
    if idx == 999:
        break
    if 0 <= idx < len(report):
        print(f"Grades for {report[idx][0]} are {report[idx][1]}")

print('PROGRAM ENDED')