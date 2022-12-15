students_data = input().split(":")

students_info = {}

while len(students_data) > 1:
    name, student_id, course_type = students_data
    name_id = [name, student_id]
    course_type = course_type.replace(" ", "_")
    if course_type in students_info:
        students_info[course_type] += name_id
    else:
        students_info[course_type] = name_id
    students_data = input().split(":")

for i in range(0, len(students_info[students_data[0]]), 2):
    print(f"{students_info[students_data[0]][i]} - {students_info[students_data[0]][i+1]}")
