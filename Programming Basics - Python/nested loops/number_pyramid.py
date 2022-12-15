n = int(input())

number = 1
cols = 1

while number <= n:
    for i in range(cols):
        if number > n:
            break
        print(number, end=" ")
        number += 1
    print()
    cols +=1
