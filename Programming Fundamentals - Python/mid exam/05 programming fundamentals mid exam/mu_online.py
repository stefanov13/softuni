def potion(potion_health, health):
    old_health = health
    health += potion_health
    if health > 100:
        health = 100
        potion_health = health - old_health
    print(f"You healed for {potion_health} hp.")
    print(f"Current health: {health} hp.")
    return health


def chest(bitcoins_amount, bitcoins):
    bitcoins += bitcoins_amount
    print(f"You found {bitcoins_amount} bitcoins.")
    return bitcoins


def monster(monster_name, health_attack, health, room_num):
    health -= health_attack
    if health > 0:
        print(f"You slayed {monster_name}.")
    else:
        print(f"You died! Killed by {monster_name}.")
        print(f"Best room: {room_num + 1}")
    return health

dungeon_rooms = input().split("|")

health = 100
bitcoins = 0

for pos, room in enumerate(dungeon_rooms):
    room = room.split()
    if room[0] == "potion":
        health = potion(int(room[-1]), health)
    elif room[0] == "chest":
        bitcoins = chest(int(room[-1]), bitcoins)
    else:
        health = monster(room[0], int(room[-1]), health, pos)
    if health <= 0:
        break

else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
