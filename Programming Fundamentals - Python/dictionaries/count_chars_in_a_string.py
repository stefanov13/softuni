word = input()

result_dict = {}

for letter in word:
    if letter in result_dict:
        result_dict[letter] += 1
    else:
        result_dict[letter] = 1

for key, value in result_dict.items():
    if not key in " ":
        print(f"{key} -> {value}")
