from unittest import result


count_ot_char = int(input())

sum_equals = 0

for _ in range(count_ot_char):
    char = input()
    sum_equals += ord(char)

print(f"The sum equals: {sum_equals}")
