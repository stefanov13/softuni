n = int(input())

count_first_group = 0
count_second_group = 0
count_third_group = 0


for _ in range(1, n + 1):
    digit = int(input())
    if digit % 2 == 0:
        count_first_group += 1
    if digit % 3 == 0:
        count_second_group += 1
    if digit % 4 == 0:
        count_third_group += 1
   

percent_result_first = (count_first_group / n) * 100
percent_result_second = (count_second_group / n) * 100
percent_result_third = (count_third_group / n) * 100


print(f"{percent_result_first:.2f}%")
print(f"{percent_result_second:.2f}%")
print(f"{percent_result_third:.2f}%")
