all_count_steps = 0

while all_count_steps < 10000:
    count_steps = input()
    if count_steps == "Going home":
        last_count_steps = int(input())
        all_count_steps += last_count_steps
        break
    else:
        all_count_steps += int(count_steps)

less_steps = 10000 - all_count_steps

if all_count_steps >= 10000:
    print("Goal reached! Good job!")
else:
    print(f"{less_steps} more steps to reach goal.")
