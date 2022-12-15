n = int(input())
l = int(input())


for num_1 in range(1, n):
    for num_2 in range(1, n):
        for letter_1 in range(97, 97 + l):
            for letter_2 in range(97, 97 + l):
                for num_3 in range(1, n + 1):
                    letter_1_as_chr = chr(letter_1)
                    letter_2_as_chr = chr(letter_2)
                    if num_3 > num_1 and num_2 < num_3:
                        print(f"{num_1}{num_2}{letter_1_as_chr}{letter_2_as_chr}{num_3}", end = " ")
