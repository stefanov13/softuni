searched_strings = input().split(", ")
string = input().split(", ")

result_list = [searched_word for searched_word in searched_strings for word in string if searched_word in word]


# for searched_word in searched_strings:
#     for word in string:
#         if searched_word in word:
#             result_list.append(searched_word)

unique_list = []
for result_word in result_list:
    if result_word not in unique_list:
        unique_list.append(result_word)

print(unique_list)
