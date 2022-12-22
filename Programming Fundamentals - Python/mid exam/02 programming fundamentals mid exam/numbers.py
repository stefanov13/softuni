sequence_list = list(map(int, input().split()))

avr_value = sum(sequence_list) / len(sequence_list)

result_list = [num for num in sequence_list if num > avr_value]
result_list.sort()
result_list = result_list[::-1]
result_list = result_list[:5]

result_print = " ".join(map(str, result_list))
if result_list == []:
    print("No")
else:    
    print(result_print)
