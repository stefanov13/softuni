def rate(position, plant_rating, all_plants):
    all_plants[position]["rating"].append(plant_rating)
    return all_plants


def update(position, rarity_for_update, all_plants):
    all_plants[position]["rarity"] = rarity_for_update
    return all_plants


def reset(position, all_plants):
    all_plants[position]["rating"] = []
    return all_plants


def is_exist(plant_name, plants_list):
    for pos, el in enumerate(plants_list):
        if plant_name in el.values():
            return True, pos
    return False, 0


def average_rating(current_plant):
    if current_plant["rating"]:
        avg_rate = sum(current_plant["rating"]) / len(current_plant["rating"])
        return avg_rate
    return 0


num_of_plants = int(input())

discovered_plants = []
for el in range(num_of_plants):
    name, rarity = input().split("<->")
    found, index = is_exist(name, discovered_plants)
    if found:
        discovered_plants[index]["rarity"] = int(rarity)
    else:
        discovered_plants.append({"plant" : name, "rarity" : int(rarity), "rating" : []})
    

action_command = input()
while not action_command == "Exhibition":
    action = action_command.split(": ")
    if action[0] == "Rate":
        plant, rating = action[1].split(" - ")
        founded, index = is_exist(plant, discovered_plants)
        if founded:
            discovered_plants = rate(index, float(rating), discovered_plants)
        else:
            print("error")
    elif action[0] == "Update":
        plant, new_rarity = action[1].split(" - ")
        founded, index = is_exist(plant, discovered_plants)
        if founded:
            discovered_plants = update(index, int(new_rarity), discovered_plants)
        else:
            print("error")
    elif action[0] == "Reset":
        founded, index = is_exist(action[1], discovered_plants)
        if founded:
            discovered_plants = reset(index, discovered_plants)
        else:
            print("error")
    action_command = input()

print("Plants for the exhibition:")
for i, d in enumerate(discovered_plants):
    average = average_rating(d)
    print(f"- {d['plant']}; Rarity: {d['rarity']}; Rating: {average:.2f}")
