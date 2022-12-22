import math

students_count = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_student_attendances = 0

for student in range(students_count):
    student_attendances = int(input())
    total_bonus = student_attendances / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_student_attendances = student_attendances

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_student_attendances} lectures.")
