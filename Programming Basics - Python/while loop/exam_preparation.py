failed_marks = int(input())

last_task_name = ""
mark_sum = 0
count_failed_marks = 0
count_task_marks = 0
stop_command = False

while count_failed_marks != failed_marks:
    task_name = input()
    if task_name == "Enough":
        stop_command = True
        break
    
    task_mark = int(input())
    mark_sum += task_mark
    
    if task_mark <= 4:
        count_failed_marks += 1
    
    count_task_marks += 1
    last_task_name = task_name
    
average_mark = mark_sum / count_task_marks

if stop_command:
    print(f"Average score: {average_mark:.2f}")
    print(f"Number of problems: {count_task_marks}")
    print(f"Last problem: {last_task_name}")
else:
    print(f"You need a break, {count_failed_marks} poor grades.")
