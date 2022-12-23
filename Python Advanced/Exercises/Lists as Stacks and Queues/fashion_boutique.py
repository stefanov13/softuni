clothes_box_stack = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_fullness = 0
rack_count = 1
for _ in range(len(clothes_box_stack)):
    current_clothing = clothes_box_stack.pop()
    if rack_fullness + current_clothing <= rack_capacity:
        rack_fullness += current_clothing
    else:
        rack_fullness = current_clothing
        rack_count += 1

print(rack_count)
