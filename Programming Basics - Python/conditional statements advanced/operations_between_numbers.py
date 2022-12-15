digit_1 = int(input())
digit_2 = int(input())
operator = input()

result = 0
even_odd_check = 0

if operator == "+":
    result = digit_1 + digit_2
elif operator == "-":
    result = digit_1 - digit_2
elif operator == "*":
    result = digit_1 * digit_2

if operator == "/" and digit_2 != 0:
    result = digit_1 / digit_2
elif operator == "%" and digit_2 != 0:
    result = digit_1 % digit_2

if operator == "+" or operator == "-" or operator == "*":
    if result % 2 == 0:
        even_odd_check = "even"
    else:
        even_odd_check = "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{digit_1} {operator} {digit_2} = {result} - {even_odd_check}")
elif operator == "/" and digit_2 != 0:
    print(f"{digit_1} {operator} {digit_2} = {result:.2f}")
elif operator == "%" and digit_2 != 0:
    print(f"{digit_1} {operator} {digit_2} = {result}")
else:
    print(f"Cannot divide {digit_1} by zero")
