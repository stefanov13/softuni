def swap(index1, index2):
    num1 = digit_list[index1]
    num2 = digit_list[index2]
    digit_list.insert(index1, num2)
    digit_list.pop(index1 + 1)
    digit_list.insert(index2, num1)
    digit_list.pop(index2 + 1)
    return digit_list


def multiply(index1, index2):
    num1 = digit_list[index1]
    num2 = digit_list[index2]
    result_num = num1 * num2
    digit_list.insert(index1, result_num)
    digit_list.pop(index1 + 1)
    return digit_list


def decrease():
    for i in range(len(digit_list)):
        digit_list[i] -= 1
    return digit_list


digit_list = list(map(int, input().split()))
operation = input()

while operation not in "end":
    operation.split()[0]
    if operation[0] in "swap":
        index1 = int(operation.split()[1])
        index2 = int(operation.split()[2])
        swap(index1, index2)
    elif operation[0] in "multiply":
        index1 = int(operation.split()[1])
        index2 = int(operation.split()[2])
        multiply(index1, index2)
    elif operation == "decrease":
        decrease()
    operation = input()

result = ", ".join(map(str, digit_list))
print(result)
