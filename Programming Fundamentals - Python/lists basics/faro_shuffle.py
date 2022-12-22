cards_for_shuffles = input().split()
shuffles_count = int(input())

half_shuffles_list = len(cards_for_shuffles) // 2


for _ in range(shuffles_count):
    first_part = []
    second_part = []
    first_part = cards_for_shuffles[:half_shuffles_list]
    second_part = cards_for_shuffles[half_shuffles_list:]
    cards_for_shuffles = []
    for elements in first_part:
        cards_for_shuffles.append(elements)
        for i, value in enumerate(second_part):
            cards_for_shuffles.append(value)
            second_part.pop(i)
            break
        continue
            

print(cards_for_shuffles)
