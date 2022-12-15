money_on_hand = float(input())
action = input()
 
while action != "mall.Enter":
    action = input()
 
action = input()
money_left = money_on_hand
purchases = 0
 
while action != "mall.Exit":
    for letter in action:
        if ord(letter) == 42: # *
            money_left += 10
#        char_value = ord(letter)
        elif money_left > 0:
            purchase_price = 0
            if letter.isupper():
                purchase_price = f'{(ord(letter) * 0.5):.2f}'
            elif letter.islower():
                purchase_price = f'{(ord(letter) * 0.3):.2f}'
            elif ord(letter) == 37:  # %
                purchase_price = f'{(money_left * 0.5):.2f}'
            else:
                purchase_price = ord(letter)

            if float(purchase_price) > money_left:
                continue

            money_left -= float(purchase_price)
            purchases += 1


    action = input()
 
if purchases == 0:
    print(f"No purchases. Money left: {money_left:.2f} lv.")
else:
    print(f"{purchases} purchases. Money left: {money_left:.2f} lv.")
 