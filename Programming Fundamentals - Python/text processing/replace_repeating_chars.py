sequence = input()
unique_string = ""
last_char = ""
for char in sequence:
    if char == last_char:
        continue
    unique_string += char
    last_char = char

print(unique_string)
