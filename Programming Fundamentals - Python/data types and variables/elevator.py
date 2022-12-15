people = int(input())
capacity = int(input())

courses = 0

if people <= capacity:
    courses = 1
else:
    if people % capacity == 0:
        courses = people // capacity
    else:
        courses = (people // capacity) + 1

print(courses)
