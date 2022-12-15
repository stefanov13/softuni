iteral_count = int(input())

start_letter = "a"

for first_letter in range(ord(start_letter), ord(start_letter) + iteral_count):
    for second_letter in range(ord(start_letter), ord(start_letter) + iteral_count):
        for thitd_letter in range(ord(start_letter), ord(start_letter) + iteral_count):
            print(chr(first_letter) + chr(second_letter) + chr(thitd_letter))
