import re

def product_group(text):
    result = ""
    for char in text:
        if char.isdigit():
            result += char
    if not result:
        return "00"
    return result

num_of_barcodes = int(input())
for _ in range(num_of_barcodes):
    barcode = input()
    pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"
    match = re.search(pattern, barcode)
    if match:
        print(f"Product group: {product_group(match.group(2))}")
    else:
        print("Invalid barcode")
