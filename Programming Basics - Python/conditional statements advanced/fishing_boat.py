grup_budget = int(input())
season = input()
fisher_count = int(input())

ship_borrow_price = 0

if season == "Spring":
    ship_borrow_price = 3000
elif season == "Winter":
    ship_borrow_price = 2600
else:
    ship_borrow_price = 4200

if fisher_count <= 6:
    ship_borrow_price *= 0.9
elif 7 <= fisher_count <= 11:
    ship_borrow_price *= 0.85
else:
    ship_borrow_price *= 0.75

if (fisher_count % 2) == 0 and season != "Autumn":
    ship_borrow_price *= 0.95

if ship_borrow_price <= grup_budget:
    print(f"Yes! You have {(grup_budget - ship_borrow_price):.2f} leva left.")
else:
    print(f"Not enough money! You need {(ship_borrow_price-grup_budget):.2f} leva.")
