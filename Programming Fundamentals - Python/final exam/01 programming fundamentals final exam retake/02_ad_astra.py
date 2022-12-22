import re

NEEDED_CALORIES = 2000  # per day
text_string = input()

pattern = re.compile(r"(#|\|)(?P<item_name>[a-zA-Z\s]+)\1(?P<expiration_date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1")
total_calories = 0
days_can_last = 0
result = [m.groupdict() for m in re.finditer(pattern, text_string)]


for d in result:
    total_calories += int(d["calories"])

days_can_last = total_calories // NEEDED_CALORIES
print(f"You have food to last you for: {days_can_last} days!")

for d in result:
    print(f"Item: {d['item_name']}, Best before: {d['expiration_date']}, Nutrition: {d['calories']}")
