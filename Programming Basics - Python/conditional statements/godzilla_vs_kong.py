movie_budget = float(input())
statists_count = int(input())
statist_wear_price = float(input())

decor_price = movie_budget * 0.1
all_wear_price = statists_count * statist_wear_price

if statists_count > 150:
    all_wear_price -= (all_wear_price * 0.1)

all_expenses = all_wear_price + decor_price

if all_expenses <= movie_budget:
    print ("Action!")
    print (f"Wingard starts filming with {movie_budget - all_expenses:.2f} leva left.")
else:
    print ("Not enough money!")
    print (f"Wingard needs {all_expenses - movie_budget:.2f} leva more.")
