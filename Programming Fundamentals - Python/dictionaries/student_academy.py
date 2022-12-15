students_grades_count = int(input())

students_academy = {}
grades_count = {}

def add_new_student(students_academy, student, grade):
    students_academy[student] = grade
    return students_academy


def count_grades(grades_count, student):
    grades_count[student] = 1
    return grades_count


def add_grade_exist_student(students_academy, student, grade):
    students_academy[student] += grade
    return students_academy


def sum_grades(grades_count, student):
    grades_count[student] += 1
    return grades_count

for _ in range(students_grades_count):
    student = input()
    grade = float(input())
    
    if not student in students_academy:
        add_new_student(students_academy, student, grade)
        count_grades(grades_count, student)
    else:
        add_grade_exist_student(students_academy, student, grade)
        sum_grades(grades_count, student)

remove_students = []

for k, v in students_academy.items():
    students_academy[k] /= grades_count[k]
    if students_academy[k] < 4.5:
        remove_students.append(k)
    
for peopele in remove_students:
    students_academy.pop(peopele)

for k, v in students_academy.items():
    print(f"{k} -> {v:.2f}")
