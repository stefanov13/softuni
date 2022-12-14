PUZZLE_PRICE = 2.60
TALKING_DOLLS_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINIONS_PRICE = 8.20
LORRYS_TOY_PRICE = 2.00


excursion_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
lorrys_toy_count = int(input())

count_all_ordered_toys = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + lorrys_toy_count
order_sum = sum([
    puzzles_count * PUZZLE_PRICE,
    talking_dolls_count * TALKING_DOLLS_PRICE,
    teddy_bears_count * TEDDY_BEAR_PRICE,
    minions_count * MINIONS_PRICE,
    lorrys_toy_count * LORRYS_TOY_PRICE
])

if count_all_ordered_toys >= 50:
    order_sum *= 0.75

profit_after_rent = order_sum * 0.9

if profit_after_rent - excursion_price >= 0:
    print(f"Yes! {(profit_after_rent - excursion_price):.2f} lv left.")
else:
    print(f"Not enough money! {(excursion_price - profit_after_rent):.2f} lv needed.")
