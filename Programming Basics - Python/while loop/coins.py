money_change = int(float(input()) *100)

coins_counter = 0


while money_change > 0:
    if (money_change - 200) >= 0:
        money_change -= 200
    elif (money_change - 100) >= 0:
        money_change -= 100
    elif (money_change - 50) >= 0:
        money_change -= 50
    elif (money_change - 20) >= 0:
        money_change -= 20
    elif (money_change - 10) >= 0:
        money_change -= 10
    elif (money_change - 5) >= 0:
        money_change -= 5
    elif (money_change - 2) >= 0:
        money_change -= 2
    elif (money_change - 1) >= 0:
        money_change -= 1
    coins_counter += 1

print(coins_counter)
