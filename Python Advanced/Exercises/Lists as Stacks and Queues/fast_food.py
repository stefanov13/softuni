from collections import deque

food_quantity = int(input())
sequence = deque(int(x) for x in input(). split())

print(max(sequence))
while sequence:
    if food_quantity >= sequence[0]:
        food_quantity -= sequence[0]
        sequence.popleft()
    else:
        break

if sequence:
    print(f"Orders left: {' '.join(map(str, sequence))}")
else:
    print("Orders complete")
