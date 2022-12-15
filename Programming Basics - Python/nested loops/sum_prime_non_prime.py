prime_digits_sum = 0
nonprime_digits_sum = 0

while True:
    command = input()
    if command == "stop":
        break
    digit = int(command)
    if digit < 0:
        print("Number is negative.")
        continue
    is_prime = True
    for i in range(2, digit):
        if digit % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_digits_sum += digit
    else:
        nonprime_digits_sum += digit

print(f"Sum of all prime numbers is: {prime_digits_sum}")
print(f"Sum of all non prime numbers is: {nonprime_digits_sum}")
