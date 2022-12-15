n = int(input())

odd_sum = 0
odd_min = 999999999
odd_max = -999999999
even_sum = 0
even_min = 999999999
even_max = -999999999



for i in range(1, (n + 1)):
    number = float(input())

    if i % 2 == 0:       
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
        even_sum += number
    else:
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
        odd_sum += number

print(f"OddSum={odd_sum:.2f},")
if odd_min != 999999999:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMin=No,")
    print("OddMax=No,")

print(f"EvenSum={even_sum:.2f},")
if even_min != 999999999:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMin=No,")
    print("EvenMax=No")
