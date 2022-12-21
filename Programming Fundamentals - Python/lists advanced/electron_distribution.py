electrons_count = int(input())
counter_electrons = electrons_count
shell = 0
result_list = []

while counter_electrons != 0:
    shell += 1
    if counter_electrons >= 2 * (shell ** 2):
        result_list.append(2 * (shell ** 2))
        counter_electrons -= result_list[shell - 1]
    else:
        result_list.append(counter_electrons)
        counter_electrons = 0

print(result_list)
