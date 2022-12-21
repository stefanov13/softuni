def sum_numbers(num_one, num_two):
    return num_one + num_two


def subtract(num_for_subtract):
    return sum_numbers(first_num, second_num) - num_for_subtract


def add_and_subtract():
    return subtract(subtract_num)


first_num = int(input())
second_num = int(input())
subtract_num = int(input())

print(add_and_subtract())
