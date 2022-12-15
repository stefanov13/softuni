month = input()
nights_count = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = nights_count * 50
    apartment_price = nights_count * 65
elif month == "June" or month == "September":
    studio_price = nights_count * 75.20
    apartment_price = nights_count * 68.70
else:
    studio_price = nights_count * 76
    apartment_price = nights_count * 77

if  7 < nights_count <= 14 and month in ["May", "October"]:
    studio_price *= 0.95
elif nights_count > 14 and month in ["May", "October"]:
    studio_price *= 0.7
elif nights_count > 14 and month in ["June", "September"]:
    studio_price *= 0.8

if nights_count > 14:
    apartment_price *= 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
