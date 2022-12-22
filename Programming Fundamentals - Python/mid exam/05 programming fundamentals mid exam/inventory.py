def item_exist(check_item, sequence):
    return check_item in sequence


def collect(add_item, sequence):
    if not item_exist(add_item, sequence):
        sequence.append(add_item)
        return sequence
    return sequence

def drop(remove_item, sequence):
    if item_exist(remove_item, sequence):
        sequence.remove(remove_item)
        return sequence
    return sequence


def renew(moving_item, sequence):
    if item_exist(moving_item, sequence):
        index_item_for_move = sequence.index(moving_item)
        item_for_move = sequence.pop(index_item_for_move)
        sequence.append(item_for_move)
        return sequence
    return sequence


def combine_items(items_for_combine, sequence):
    items_for_combine = items_for_combine.split(":")
    exist_item = items_for_combine[0]
    add_item = items_for_combine[1]
    if item_exist(exist_item, sequence):
        index_exist_item = sequence.index(exist_item)
        sequence.insert(index_exist_item + 1, add_item)
        return sequence
    return sequence


journal = input().split(", ")
given_action = input()

while not given_action == "Craft!":
    command_for_menage = given_action.split(" - ")[0]
    item_for_menage = given_action.split(" - ")[1]
    if command_for_menage == "Collect":
        journal = collect(item_for_menage, journal)
    elif command_for_menage == "Drop":
        journal = drop(item_for_menage, journal)
    elif command_for_menage == "Renew":
        journal = renew(item_for_menage, journal)
    elif command_for_menage == "Combine Items":
        journal = combine_items(item_for_menage, journal)
    given_action = input()

print(", ".join(journal))
