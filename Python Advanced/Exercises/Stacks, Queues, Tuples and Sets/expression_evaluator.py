from collections import deque

def operation(summary, queue, operator):
    num_1 = queue.popleft()
    num_2 = None
    if queue:
        num_2 = queue.popleft()
    if num_2:
        if operator == "-":
            summary = summary - num_1 - num_2
        elif operator == "+":
            summary = summary + num_1 + num_2
        elif operator == "*":
            summary = summary * num_1 * num_2
        elif operator == "/":
            summary = summary // num_1 // num_2
    else:
        if operator == "-":
            summary = summary - num_1
        elif operator == "+":
            summary = summary + num_1
        elif operator == "*":
            summary = summary * num_1
        elif operator == "/":
            summary = summary // num_1
    return summary


sequence_ = input().split()
temp_queue = deque()
result_ = None

for i, el in enumerate(sequence_):
    sign = ("+", "-", "*", "/")
    if el.isdigit() and i == 0:
        result_ = int(el)
    elif el.isdigit():
        temp_queue.append(int(el))
    elif el in sign:
        result_ = operation(result_, temp_queue, el)
    else:
        if i == 0:
            result_ = int(el)
        else:
            temp_queue.append(int(el))


print(result_)
