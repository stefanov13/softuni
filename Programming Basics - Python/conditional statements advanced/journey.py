budget = float(input())
season = input()

price = 0
vacation_place = ""
vacation_type = ""

if budget <= 100:
    vacation_place = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
    else:
        price = budget * 0.7
elif budget <= 1000:
    vacation_place = "Balkans"
    if season == "summer":
        price = budget * 0.4
    else:
        price = budget * 0.8
else:
    vacation_place = "Europe"
    price = budget * 0.9

if season == "summer" and vacation_place != "Europe":
    vacation_type = "Camp"
else:
    vacation_type = "Hotel"

print(f"Somewhere in {vacation_place}")
print(f"{vacation_type} - {price:.2f}")
