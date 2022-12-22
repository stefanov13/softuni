the_string = input().split()
result = []

for element in the_string:
    element = int(element)
    if element >= 0:
        element -= (element * 2)
        result.append(element)
    else:
        element = abs(element)
        result.append(element) 

print(result)
