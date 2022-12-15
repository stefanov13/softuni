materials_dict = {"shards":0, "fragments":0, "motes":0}


while True:
    materials = input().lower().split()
    key = False
    for material in range(1, len(materials), 2):
        if materials[material] in materials_dict:
            materials_dict[materials[material]] += int(materials[material-1])
            if materials_dict["shards"] >= 250:
                break
            elif materials_dict["fragments"] >= 250:
                break
            elif materials_dict["motes"] >= 250:
                break
        else:
            materials_dict[materials[material]] = int(materials[material-1])
            if materials_dict["shards"] >= 250:
                break
            elif materials_dict["fragments"] >= 250:
                break
            elif materials_dict["motes"] >= 250:
                break

    if materials_dict["shards"] >= 250:
        materials_dict["shards"] -= 250
        print("Shadowmourne obtained!")
        break
    elif materials_dict["fragments"] >= 250:
        materials_dict["fragments"] -= 250
        print("Valanyr obtained!")
        break
    elif materials_dict["motes"] >= 250:
        materials_dict["motes"] -= 250
        print("Dragonwrath obtained!")
        break
    
    

for k, v  in materials_dict.items():
    print(f"{k}: {v}")
