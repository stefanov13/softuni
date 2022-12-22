part_price = input()

prices = []

while part_price not in("special", "regular"):
    if float(part_price) < 0:
        print("Invalid price!")
    else:
        prices.append(float(part_price))
    part_price = input()
    

prices_sum = sum(prices)
taxes = prices_sum * 0.2
total_prices = prices_sum + taxes

if prices:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {prices_sum:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if part_price == "special":
        total_prices -= total_prices / 10
        print(f"Total price: {total_prices:.2f}$")
    else:
        print(f"Total price: {total_prices:.2f}$")
else:
    print("Invalid order!")
