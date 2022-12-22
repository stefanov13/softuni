factor = int(input())
count = int(input())
the_list = []

for i in range(1, count + 1):
    result = factor * i
    the_list.append(result)

print(the_list)
