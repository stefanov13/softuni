from collections import deque

def check_milkshakes(milk_ingredient, chocolate_ingredient):
    count = 0
    while chocolate_ingredient and milk_ingredient and count != 5:
        choco = chocolate_ingredient.pop()
        milk = milk_ingredient.popleft()

        if choco <= 0 and milk <= 0:
            continue
        elif choco <= 0:
            milk_ingredient.appendleft(milk)
            continue
        elif milk <= 0:
            chocolate_ingredient.append(choco)
            continue

        if choco == milk:
            count += 1
        else:
            milk_ingredient.append(milk)
            chocolate_ingredient.append(choco - 5)

    return count, milk_ingredient, chocolate_ingredient


chocolate = [int(num) for num in input().split(", ")]
milk_cups = deque(int(num) for num in input().split(", "))

milkshakes_count, milk_cups, chocolate = check_milkshakes(milk_cups, chocolate)

if milkshakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print("Milk: empty")
