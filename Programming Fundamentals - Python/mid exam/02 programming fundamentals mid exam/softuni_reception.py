all_employees_per_hour = 0
for i in range(3):
    all_employees_per_hour += int(input())
students_count = int(input())
all_needed_time = 0

while students_count > 0:
    all_needed_time += 1
    students_count -= all_employees_per_hour
    if (all_needed_time + 1) % 4 == 0 and students_count > 0:
        all_needed_time += 1
        
print(f"Time needed: {all_needed_time}h.")
