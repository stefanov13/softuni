def check_availability(place, plunder_target):
    for index, town in enumerate(plunder_target):
        if place in town["settlement"]:
            return True, index
    return False, 0


def plunder(place, count_of_people, tresor, plunder_target):
    is_there, index = check_availability(place, plunder_target)
    plunder_target[index]["population"] -= count_of_people
    plunder_target[index]["gold"] -= tresor
    print(f"{place} plundered! {tresor} gold stolen, {count_of_people} citizens killed.")
    if plunder_target[index]["population"] <= 0 or plunder_target[index]["gold"] <= 0:
        plunder_target.pop(index)
        print(f"{place} has been wiped off the map!")
    return plunder_target


def prosper(place, tresor, plunder_target):
    if tresor < 0:
        print("Gold added cannot be a negative number!")
        return plunder_target
    is_there, index = check_availability(place, plunder_target)
    plunder_target[index]["gold"] += tresor
    total_gold = plunder_target[index]["gold"]
    print(f"{tresor} gold added to the city treasury. {place} now has {total_gold} gold.")
    return plunder_target


def get_data():
    targets = []
    while True:
        target = input()
        if target == "End":
            break
        city_data = target.split("||")
        events = target.split("=>")
        if len(city_data) > 1:
            town, population, gold = city_data
            is_exist, index_num = check_availability(town, targets)
            if is_exist:
                targets[index_num]["population"] += int(population)
                targets[index_num]["gold"] += int(gold)
                continue
            targets.append({"settlement":town, "population":int(population), "gold":int(gold)})
            continue
        elif len(events) > 1:
            if events[0] == "Plunder":
                town = events[1]
                people = int(events[2])
                gold = int(events[3])
                targets = plunder(town, people, gold, targets)
            elif events[0] == "Prosper":
                town = events[1]
                gold = int(events[2])
                targets = prosper(town, gold, targets)
    print_result(targets)
    return targets
        


def print_result(targets_left):
    if targets_left:
        print(f"Ahoy, Captain! There are {len(targets_left)} wealthy settlements to go to:")
        for left_target in targets_left:
            print(f'{left_target["settlement"]} -> Population: {left_target["population"]} citizens, Gold: {left_target["gold"]} kg')
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


result = get_data()
