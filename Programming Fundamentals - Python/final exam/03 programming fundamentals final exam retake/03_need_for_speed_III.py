def position(vehicle, car_fleet):
    for pos, d in enumerate(car_fleet):
        if d["car"] == vehicle:
            return pos


def drive(vehicle, journey, fuel_needed, car_fleet):
    index_pos = position(vehicle, car_fleet)
    current_car = car_fleet[index_pos]
    if current_car["car"] == vehicle and current_car["fuel"] >= fuel_needed:
        current_car["mileage"] += journey
        current_car["fuel"] -= fuel_needed
        print(f"{vehicle} driven for {journey} kilometers. {fuel_needed} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")

    if current_car["mileage"] >= 100000:
        selled_car = car_fleet.pop(index_pos)
        print(f"Time to sell the {selled_car['car']}!")
    return car_fleet



def refuel(vehicle, refuel_quantity, car_fleet):
    index_pos = position(vehicle, car_fleet)
    current_car = car_fleet[index_pos]
    if current_car["car"] == vehicle and current_car["fuel"] + refuel_quantity <= 75:
        current_car["fuel"] += refuel_quantity
        added_fuel = refuel_quantity
    else:
        added_fuel = 75 - current_car["fuel"]
        current_car["fuel"] = 75
    print(f"{vehicle} refueled with {added_fuel} liters")
    return car_fleet


def revert(vehicle, revert_kilometers, car_fleet):
    index_pos = position(vehicle, car_fleet)
    current_car = car_fleet[index_pos]
    if current_car["car"] == vehicle and current_car["mileage"] - revert_kilometers < 10000:
        current_car["mileage"] = 10000
    else:
        current_car["mileage"] -= revert_kilometers
        print(f"{vehicle} mileage decreased by {revert_kilometers} kilometers")
    return car_fleet


 
cars_count = int(input())
available_cars = []
for car in range(cars_count):
    car_manufacturer, car_mileage, fuel_quantity = input().split("|")
    available_cars.append({"car" : car_manufacturer, "mileage": int(car_mileage), "fuel" : int(fuel_quantity)})

command = input()
while not command == "Stop":
    action = command.split(" : ")[0]
    if action == "Drive":
        car_name = command.split(" : ")[1]
        distance = command.split(" : ")[2]
        fuel = command.split(" : ")[3]
        available_cars = drive(car_name, int(distance), int(fuel), available_cars)
    elif action == "Refuel":
        car_name = command.split(" : ")[1]
        fuel = command.split(" : ")[2]
        available_cars = refuel(car_name, int(fuel), available_cars)

    elif action == "Revert":
        car_name = command.split(" : ")[1]
        kilometers = command.split(" : ")[2]
        available_cars = revert(car_name, int(kilometers), available_cars)

    command = input()

for result_dict in available_cars:
    print(f"{result_dict['car']} -> Mileage: {result_dict['mileage']} kms, Fuel in the tank: {result_dict['fuel']} lt.")
