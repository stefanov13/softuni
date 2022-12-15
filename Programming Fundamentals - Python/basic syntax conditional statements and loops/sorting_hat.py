while True:
    student_name = input()
    if student_name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif student_name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif len(student_name) < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif len(student_name) == 5:
        print(f"{student_name} goes to Slytherin.")
    elif len(student_name) == 6:
        print(f"{student_name} goes to Ravenclaw.")
    else:
        print(f"{student_name} goes to Hufflepuff.")
