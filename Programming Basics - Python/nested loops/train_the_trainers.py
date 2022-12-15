jury_count =  int(input())

sum_all_presentation_grade = 0
average_all_presentation_grade = 0
presentation_count = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    average_presentation_grade = 0
    sum_presentation_grade = 0

    for grade_count in range(jury_count):
        grade = float(input())
        sum_presentation_grade += grade
    
    average_presentation_grade = sum_presentation_grade / jury_count
    sum_all_presentation_grade += average_presentation_grade
    presentation_count += 1

    print(f"{presentation_name} - {average_presentation_grade:.2f}.")

average_all_presentation_grade = sum_all_presentation_grade / presentation_count
print(f"Student's final assessment is {average_all_presentation_grade:.2f}.")
