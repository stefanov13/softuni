def char_in_range(start_char, end_char):
    result = []
    for i in range(ord(start_char) + 1, ord(end_char)):
        result.append(chr(i))
    return ' '.join(map(str, result))
     


first_char = input()
second_char = input()

print(char_in_range(first_char, second_char))
