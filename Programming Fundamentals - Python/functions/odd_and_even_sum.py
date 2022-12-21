num_as_string = input()
nums = [int(num) for num in num_as_string]
sum_even_nums = sum(list(filter(lambda x: x % 2 == 0, nums)))
sum_odd_nums = sum(list(filter(lambda x: x % 2 != 0, nums)))
print(f"Odd sum = {sum_odd_nums}, Even sum = {sum_even_nums}")


# odd_num = 0
# even_num = 0

# str_num = input()

# def split_string(str_num):
#     num_list =[]
#     for i in str_num:
#         num_list.append(i)
#     return num_list

# num_list = split_string(str_num)


# def odd(odd_num):
#     for num in num_list:
#         if int(num) % 2 != 0:
#             odd_num += int(num)
#     return odd_num


# def even(even_num):
#     for num in num_list:
#         if int(num) % 2 == 0:
#             even_num += int(num)
#     return even_num


# print(f"Odd sum = {odd(odd_num)}, Even sum = {even(even_num)}")
