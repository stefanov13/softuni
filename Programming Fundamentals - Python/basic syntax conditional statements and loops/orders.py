orders_count = int(input())
total_price = 0

for _ in range(orders_count):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.0:
        continue
    elif days < 1 or days > 31:
        continue
    elif needed_capsules_per_day < 1 or needed_capsules_per_day > 2000:
        continue
    
    total_price += price_per_capsule * needed_capsules_per_day * days
    print(f"The price for the coffee is: ${price_per_capsule * needed_capsules_per_day * days:.2f}")

print(f"Total: ${total_price:.2f}")
