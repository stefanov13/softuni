collection_of_items = input().split('|')
budget = float(input())
sold_items = 0
total_profit = 0
list_sold_items_price = []
for item in collection_of_items:
    increase_item_price = 1.4
    profit = 0
    separate_string_float = item.split('->')
    float_item_value = float(separate_string_float[1])
    string_item_value = separate_string_float[0]
    if string_item_value == 'Clothes' and float_item_value <= 50 and float_item_value <= budget:
        budget -= float_item_value
        increase_item_price *= float_item_value
        if increase_item_price <= 0:
            increase_item_price = 40.00
        profit = increase_item_price - float_item_value
        list_sold_items_price.append(increase_item_price)
        sold_items += increase_item_price
    elif string_item_value == 'Shoes' and float_item_value <= 35 and float_item_value <= budget:
        budget -= float_item_value
        increase_item_price *= float_item_value
        if increase_item_price <= 0:
            increase_item_price = 40.00
        profit = increase_item_price - float_item_value
        list_sold_items_price.append(increase_item_price)
        sold_items += increase_item_price
    elif string_item_value == 'Accessories' and float_item_value <= 20.5 and float_item_value <= budget:
        budget -= float_item_value
        increase_item_price *= float_item_value
        if increase_item_price <= 0:
            increase_item_price = 40.00
        profit = increase_item_price - float_item_value
        list_sold_items_price.append(increase_item_price)
        sold_items += increase_item_price
    total_profit += profit
for el in list_sold_items_price:
    print(f"{el:.2f}", end=" ")
print(f"\nProfit: {round(total_profit,2)}")
if (sold_items + budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
