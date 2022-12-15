needed_money = float(input())
available_money = float(input())

spend_counter = 0
all_days_counter = 0
spend_limit = False


while needed_money > available_money:
    mouey_operation = input()
    operation_amount = float(input())
    all_days_counter += 1

    if mouey_operation == "spend":
        available_money -= operation_amount
        spend_counter += 1
        if available_money < 0:
            available_money = 0
        if spend_counter == 5:
            spend_limit = True
            break
    else:
        available_money += operation_amount
        spend_counter = 0
       

if spend_limit:
    print(f"You can't save the money.")
    print(all_days_counter)
else:
    print(f"You saved the money for {all_days_counter} days.")
