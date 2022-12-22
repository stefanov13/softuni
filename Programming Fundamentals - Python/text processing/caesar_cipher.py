string_for_encrypted = input()
encrypted_string = ""

for char in string_for_encrypted:
    encrypted_string += chr(ord(char) + 3)

print(encrypted_string)
