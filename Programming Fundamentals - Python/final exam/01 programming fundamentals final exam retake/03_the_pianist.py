def add_piece(piece_for_add, current_pieces, current_composers, current_keys):
    if not piece_for_add[0] in current_pieces:
        current_pieces.append(piece_for_add[0])
        current_composers.append(piece_for_add[1])
        current_keys.append(piece_for_add[2])
        print(f"{piece_for_add[0]} by {piece_for_add[1]} in {piece_for_add[2]} added to the collection!")
        return current_pieces, current_composers, current_keys
    print(f"{piece_for_add[0]} is already in the collection!")
    return current_pieces, current_composers, current_keys


def remove_piece(piece_for_remove, current_pieces, current_composers, current_keys):
    if piece_for_remove in current_pieces:
        piece_for_remove_index = current_pieces.index(piece_for_remove)
        current_pieces.remove(piece_for_remove)
        current_composers.pop(piece_for_remove_index)
        current_keys.pop(piece_for_remove_index)
        print(f"Successfully removed {piece_for_remove}!")
        return current_pieces, current_composers, current_keys
    print(f"Invalid operation! {piece_for_remove} does not exist in the collection.")
    return current_pieces, current_composers, current_keys


def change_key(piece_for_change_key, current_pieces, current_keys):
    if piece_for_change_key[0] in current_pieces:
        piece_for_change_key_index = current_pieces.index(piece_for_change_key[0])
        current_keys.insert(piece_for_change_key_index, piece_for_change_key[1])
        current_keys.pop(piece_for_change_key_index+1)
        print(f"Changed the key of {piece_for_change_key[0]} to {piece_for_change_key[1]}!")
        return current_keys
    print(f"Invalid operation! {piece_for_change_key[0]} does not exist in the collection.")
    return current_keys


available_pieces = {"piece" : [], "composer" : [], "key" : []}

number_of_pieces = int(input())
for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    available_pieces["piece"].append(piece)
    available_pieces["composer"].append(composer)
    available_pieces["key"].append(key)

action_command = input()
while not action_command == "Stop":
    action = action_command.split("|")[0]
    if action == "Add":
        action_command = action_command.split("|")[1:]
        available_pieces["piece"], available_pieces["composer"], available_pieces["key"] = add_piece(action_command, available_pieces["piece"], available_pieces["composer"], available_pieces["key"])
    elif action == "Remove":
        action_command = action_command.split("|")[1]
        available_pieces["piece"], available_pieces["composer"], available_pieces["key"] = remove_piece(action_command, available_pieces["piece"], available_pieces["composer"], available_pieces["key"])
    elif action == "ChangeKey":
        action_command = action_command.split("|")[1:]
        available_pieces["key"] = change_key(action_command, available_pieces["piece"], available_pieces["key"])
    action_command = input()

if available_pieces["piece"]:
    for i in range(len(available_pieces["piece"])):
        print(f"{available_pieces['piece'][i]} -> Composer: {available_pieces['composer'][i]}, Key: {available_pieces['key'][i]}")
