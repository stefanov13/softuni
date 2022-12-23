names_count = int(input())

even_set = set()
odd_set = set()

for i in range(names_count):
    name = input()
    name_ascii_sum = 0
    for char in name:
        name_ascii_sum += ord(char)
    divided_name_sum = name_ascii_sum // (i + 1)
    if divided_name_sum % 2 == 0:
        even_set.add(divided_name_sum)
    else:
        odd_set.add(divided_name_sum)

odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)


if odd_set_sum == even_set_sum:
    union_values = odd_set.union(even_set)
    print(*union_values, sep=", ")
elif odd_set_sum > even_set_sum:
    different_values = odd_set.difference(even_set)
    print(*different_values, sep=", ")
else:
    symmetric_different_values = odd_set.symmetric_difference(even_set)
    print(*symmetric_different_values, sep=", ")
