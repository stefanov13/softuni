courses = {}

course_user = input().split(" : ")

while not course_user[0] == "end":
    if not course_user[0] in courses:
        courses[course_user[0]] = [course_user[1]]
    else:
        students = courses[course_user[0]]
        students.append(course_user[1])
        courses[course_user[0]] = students

    course_user = input().split(" : ")

for k, v in courses.items():
    print(f"{k}: {len(v)}")
    for name in v:
        print(f"-- {name}")
