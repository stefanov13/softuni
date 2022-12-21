nums_for_check = input().split(", ")

result = list(map(lambda x: x == x[::-1], nums_for_check))

for el in result:
    print(el)


# str_num = input()

# def split_to_list(str_num):
#     list_num = str_num.split(", ")
#     return list_num

# list_num = split_to_list(str_num)
# checked_list = []

# def palindrome_check(list_num):
#     for element in list_num:
#         mirrored = "".join(reversed(element))
#         if element == mirrored:
#             checked_list.append("True")
#         else:
#             checked_list.append("False")
#     return checked_list


# palindrome_check(list_num)

# for i in checked_list:
#     print(i)
