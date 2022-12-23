from collections import deque

text = deque(input().split())

searched_colors = ("red", "yellow", "blue", "orange", "purple", "green")
found_colors = []

while text:
    last_substr = ""
    first_substr = text.popleft()
    if text:
        last_substr = text.pop()
        current_result = first_substr + last_substr
        switched_current_result = last_substr + first_substr
    else:
        current_result = first_substr
        switched_current_result = ""
    if current_result in searched_colors:
        found_colors.append(current_result)
    elif switched_current_result in searched_colors:
        found_colors.append(switched_current_result)
    elif not last_substr:
        continue
    else:
        middle_point = len(text) // 2
        modified_first_substr = first_substr[:-1]
        modified_last_substr = last_substr[:-1]
        if modified_first_substr:
            text.insert(middle_point, modified_first_substr)
        if modified_last_substr:
            text.insert(middle_point, modified_last_substr)


if any(["red" not in found_colors, "yellow" not in found_colors]):
    if "orange" in found_colors:
        found_colors.remove("orange")
if any(["red" not in found_colors, "blue" not in found_colors]):
    if "purple" in found_colors:
        found_colors.remove("purple")
if any(["yellow" not in found_colors, "blue" not in found_colors]):
    if "green" in found_colors:
        found_colors.remove("green")
    

print(found_colors)
