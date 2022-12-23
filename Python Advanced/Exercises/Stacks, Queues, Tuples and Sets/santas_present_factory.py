from collections import deque

def is_price_match(level, presents_group):
    is_magic = False
    for gift_type, price_quantity in presents_group.items():
        if level in price_quantity:
            is_magic = True
    return is_magic


def is_magic_gift(level, presents_group):
    for gift_type, price_quantity in presents_group.items():
        if level in price_quantity:
            presents_group[gift_type][level] += 1
    return presents_group


manufacturing_materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())

magic_presents = {
    "Doll":{150:0},
    "Wooden train":{250:0},
    "Teddy bear":{300:0},
    "Bicycle":{400:0}
}

while manufacturing_materials and magic_level:
    current_material = manufacturing_materials.pop()
    current_magic = magic_level.popleft()
    if current_material == 0 and current_magic == 0:
        continue
    elif current_material == 0:
        magic_level.appendleft(current_magic)
        continue
    elif current_magic == 0:
        manufacturing_materials.append(current_material)
        continue
    total_magic_level = current_material * current_magic
    if total_magic_level < 0:
        product_sum = current_material + current_magic
        manufacturing_materials.append(product_sum)
    elif is_price_match(total_magic_level, magic_presents):
        magic_presents = is_magic_gift(total_magic_level, magic_presents)
    else:
        manufacturing_materials.append(current_material + 15)

if magic_presents["Doll"][150] > 0 and magic_presents["Wooden train"][250] > 0:
    print("The presents are crafted! Merry Christmas!")
elif magic_presents["Teddy bear"][300] > 0 and magic_presents["Bicycle"][400] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if manufacturing_materials:
    manufacturing_materials_length = len(manufacturing_materials)
    print(f'Materials left: ', end="")
    for i in range(manufacturing_materials_length):
        material = manufacturing_materials.pop()
        if i == manufacturing_materials_length - 1:
            print(material)
        else:
            print(material, end=", ")

if magic_level:
    print(f'Magic left: {", ".join(str(x) for x in magic_level)}')

sorted_magic_presents = dict(sorted(magic_presents.items()))
for toy, quantity_dict in sorted_magic_presents.items():
    for price, quantity in quantity_dict.items():
        if quantity:
            print(f"{toy}: {quantity}")      
