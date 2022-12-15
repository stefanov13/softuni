products_dict = {}


item = input().split()

def add_new_item(products_dict, item):
    products_dict[item[0]] = [float(item[1]), int(item[2])]
    return products_dict


def sum_exist_item(products_dict, item):
    new_price = float(item[1])
    new_quantity = int(item[2])
    old_products = products_dict[item[0]]
    sum_quantity = old_products[1] + new_quantity
    products_dict[item[0]] = [new_price, sum_quantity]
    return products_dict


while not item[0] == "buy":
    if not item[0] in products_dict:
        add_new_item(products_dict, item)
    else:
        sum_exist_item(products_dict, item)
    item = input().split()

for k, v in products_dict.items():
    price, quantity = v
    total_price = price * quantity
    print(f"{k} -> {total_price:.2f}")
