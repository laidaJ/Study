student_heights = input("Input a list of student heights\n").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(student_heights)

sum_height = 0

for student_height in student_heights:
    sum_height += student_height

student_number = 0

for student in student_heights:
    student_number += 1
average_height = sum_height / student_number
print(average_height)
