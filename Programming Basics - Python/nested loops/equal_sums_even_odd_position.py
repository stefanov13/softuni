first_digit = int(input())
last_digit = int(input())


for num in range(first_digit, last_digit + 1):
    num_as_string = str(num)
    odd_sum = 0
    even_sum = 0

    for i in range(0, len(num_as_string)):
        digit = int(num_as_string[i])
        if (i + 1) % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(num, end=" ")
