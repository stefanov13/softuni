n = int(input())

count_first_group = 0
count_second_group = 0
count_third_group = 0
count_fourth_group = 0
count_fifth_group = 0


for _ in range(1, n + 1):
    digit = int(input())
    if digit < 200:
        count_first_group += 1
    elif 200 <= digit < 400:
        count_second_group += 1
    elif 400 <= digit < 600:
        count_third_group += 1
    elif 600 <= digit < 800:
        count_fourth_group += 1
    else:
        count_fifth_group += 1

percent_result_first = (count_first_group / n) * 100
percent_result_second = (count_second_group / n) * 100
percent_result_third = (count_third_group / n) * 100
percent_result_fourth = (count_fourth_group / n) * 100
percent_result_fifth = (count_fifth_group / n) * 100

print(f"{percent_result_first:.2f}%")
print(f"{percent_result_second:.2f}%")
print(f"{percent_result_third:.2f}%")
print(f"{percent_result_fourth:.2f}%")
print(f"{percent_result_fifth:.2f}%")
