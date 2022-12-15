time_of_pour = int(input())

water_tank_filled_cpacity = 0
free_capacity = 255
for pour in range(time_of_pour):
    water_quantity = int(input())
    if water_quantity > free_capacity:
        print("Insufficient capacity!")
    else:
        free_capacity -= water_quantity
        water_tank_filled_cpacity += water_quantity

print(water_tank_filled_cpacity)
