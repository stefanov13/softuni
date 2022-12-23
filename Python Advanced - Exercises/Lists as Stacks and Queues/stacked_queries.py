queries_count = int(input())

my_stack = []

for _ in range(queries_count):
    query = [int(x) for x in input().split()]
    if query[0] == 1:
        my_stack.append(query[1])
    elif query[0] == 2 and my_stack:
        my_stack.pop()
    elif query[0] == 3 and my_stack:
        print(max(my_stack))
    elif query[0] == 4 and my_stack:
        print(min(my_stack))
        
stack_len = len(my_stack)
for i in range(stack_len):
    if not i == stack_len - 1:
        print(my_stack.pop(), end= ', ')
    else:
        print(my_stack.pop())
