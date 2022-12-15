start_char_index = int(input())
end_char_index = int(input())

result_string = ""
for char in range(start_char_index, end_char_index + 1):
    result_string += chr(char)

print(" ".join(result_string))
