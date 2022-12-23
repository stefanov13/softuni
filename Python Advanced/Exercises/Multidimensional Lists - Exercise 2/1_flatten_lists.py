line = input().split("|")
result_list = []

for _ in range(len(line)):
    sub_list = line.pop()
    result_list.extend(sub_list.split())

print(*result_list)
