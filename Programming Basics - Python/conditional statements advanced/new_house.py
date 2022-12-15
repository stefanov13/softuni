flowers_type = input()
flowers_count = int(input())
budget = int(input())

flower_price = 0

if flowers_type == "Roses":
    flower_price = flowers_count * 5 
    if flowers_count > 80:
        flower_price *= 0.9      
elif flowers_type == "Dahlias":
    flower_price = flowers_count * 3.8
    if flowers_count > 90:
        flower_price *= 0.85
elif flowers_type == "Tulips":
    flower_price = flowers_count * 2.8
    if flowers_count > 80:
        flower_price *= 0.85       
elif flowers_type == "Narcissus":
    flower_price = flowers_count * 3
    if flowers_count < 120:
        flower_price *= 1.15       
elif flowers_type == "Gladiolus":
    flower_price = flowers_count * 2.5
    if flowers_count < 80:
        flower_price *= 1.2

if flower_price <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {(budget - flower_price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(flower_price - budget):.2f} leva more.")