def position_check(hero_name, all_heroes):
    for pos, d in enumerate(all_heroes):
        if d["hero_name"] == hero_name:
            return pos


def cast_spell(hero_name, mana_points_needed, spell_name, all_heroes):
    position_index = position_check(hero_name, all_heroes)
    if all_heroes[position_index]['mp'] >= mana_points_needed:
        all_heroes[position_index]['mp'] -= mana_points_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {all_heroes[position_index]['mp']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return all_heroes


def take_damage(hero_name, hit_points_damage, attacker, all_heroes):
    position_index = position_check(hero_name, all_heroes)
    all_heroes[position_index]['hp'] -= hit_points_damage
    if all_heroes[position_index]['hp'] <= 0:
        print(f"{hero_name} has been killed by {attacker}!")
        all_heroes.pop(position_index)
    else:
        print(f"{hero_name} was hit for {hit_points_damage} HP by {attacker} and now has {all_heroes[position_index]['hp']} HP left!")
    return all_heroes


def recharge(hero_name, mana_points_amount, all_heroes):
    position_index = position_check(hero_name, all_heroes)
    if all_heroes[position_index]['mp'] + mana_points_amount > 200:
        mana_points_amount = 200 - all_heroes[position_index]['mp']
        all_heroes[position_index]['mp'] = 200
    else:
        all_heroes[position_index]['mp'] += mana_points_amount
    print(f"{hero_name} recharged for {mana_points_amount} MP!")
    return all_heroes


def heal(hero_name, hit_points_amount, all_heroes):
    position_index = position_check(hero_name, all_heroes)
    if all_heroes[position_index]['hp'] + hit_points_amount > 100:
        hit_points_amount = 100 - all_heroes[position_index]['hp']
        all_heroes[position_index]['hp'] = 100
    else:
        all_heroes[position_index]['hp'] += hit_points_amount
    print(f"{hero_name} healed for {hit_points_amount} HP!")
    return all_heroes


chosen_heroes = []
num_chosen_heroes = int(input())
for _ in range(num_chosen_heroes):
    chosen_heroes_name, hit_points, mana_points = input().split()
    chosen_heroes.append({"hero_name" : chosen_heroes_name, "hp" : int(hit_points), "mp": int(mana_points)})

command = input()
while not command == "End":
    action = command.split(" - ")[0]
    parameters = command.split(" - ", 1)[1]
    if action == "CastSpell":
        name, mp_needed, spell = parameters.split(" - ")
        chosen_heroes = cast_spell(name, int(mp_needed), spell, chosen_heroes)
    elif action == "TakeDamage":
        name, damage, attacker = parameters.split(" - ")
        chosen_heroes = take_damage(name, int(damage), attacker, chosen_heroes)
    elif action == "Recharge":
        name, mp_amount = parameters.split(" - ")
        chosen_heroes = recharge(name, int(mp_amount), chosen_heroes)
    elif action == "Heal":
        name, hp_amount = parameters.split(" - ")
        chosen_heroes = heal(name, int(hp_amount), chosen_heroes)
    command = input()

for hero in chosen_heroes:
    print(f"{hero['hero_name']}")
    print(f"  HP: {hero['hp']}")
    print(f"  MP: {hero['mp']}")
