number_student = int(input('Enter n = '))

current_student = 1

summary = 0

while True:
    mark=int(input(f'Enter mark of student #{current_student} = '))

    if 0 < mark < 100:
        summary += mark
        current_student += 1
    if current_student > number_student:
        break

print(summary/number_student)