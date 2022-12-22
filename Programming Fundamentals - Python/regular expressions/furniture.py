import re

pattern_key = r"^>>(?P<furniture_name>\w+)<<(?P<price>\d+\.?\d*)\!(?P<quantity>\d+$)"
purchase_info = input()
total_sum = 0
items = []


while not purchase_info == "Purchase":
    dates = re.match(pattern_key, purchase_info)
    if dates:
        valid_purchase_info = dates.groupdict()
        total_sum += float(valid_purchase_info["price"]) * int(valid_purchase_info["quantity"])
        items.append(valid_purchase_info["furniture_name"])
    purchase_info = input()

print("Bought furniture:")
for name in items:
    print(name)
print(f"Total money spend: {total_sum:.2f}")
