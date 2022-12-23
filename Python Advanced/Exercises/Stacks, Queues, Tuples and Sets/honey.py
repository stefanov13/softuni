from collections import deque

def honey_making(bee, pollen, sign):
    if sign == "+":
        result_ = bee + pollen
    elif sign == "-":
        result_ = bee - pollen
    elif sign == "*":
        result_ = bee * pollen
    else:
        result_ = bee / pollen
    return abs(result_)


working_bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
action_symbols = deque(input().split())
total_honey = 0


while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar < current_bee:
        working_bees.appendleft(current_bee)
        continue
    if current_nectar > 0:
        current_symbol = action_symbols.popleft()
        total_honey += honey_making(current_bee, current_nectar, current_symbol)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
