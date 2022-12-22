def sum_multiplied_char(bigest, smaller):
    multiplied_sum = 0
    last_part_bigest_string = bigest[len(smaller):]
    for i in range(len(smaller)):
        multiplied_sum += ord(bigest[i]) * ord(smaller[i])
    for char in last_part_bigest_string:
            multiplied_sum += ord(char)
    return multiplied_sum


a_string = input()

first_item, second_item = a_string.split()

if len(first_item) > len(second_item):
    result = sum_multiplied_char(first_item, second_item)
else:
    result = sum_multiplied_char(second_item, first_item)

print(result)
