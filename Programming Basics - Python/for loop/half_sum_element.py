max_num = -9999999999
sum_numbers = 0

count = int(input())

for digit in range(0, count):
    num = int(input())

    if num > max_num:
        max_num = num
    
    sum_numbers += num

sum_numbers -= max_num

if sum_numbers == max_num:
    print("Yes")
    print(f"Sum = {sum_numbers}")
else:
    print("No")
    print(f"Diff = {abs(max_num - sum_numbers)}")
