def contains(searched_str, raw_key):
    if searched_str in raw_key:
        return f"{raw_key} contains {searched_str}"
    return "Substring not found!"


def flip(char_case, first_index, last_index_exc, raw_key):
    cuted_part = raw_key[first_index:last_index_exc]
    if char_case == "Upper":
        cuted_part = cuted_part.upper()
    elif char_case == "Lower":
        cuted_part = cuted_part.lower()
    raw_key = raw_key[:first_index] + cuted_part + raw_key[last_index_exc:]
    return raw_key


def remove_char(first_index, last_index_exc, raw_key):
    final_result = "".join([raw_key[i] for i in range(len(raw_key)) if i < first_index or i >= last_index_exc])
    return final_result


def main_action(raw_key):
    while True:
        action_command = input().split(">>>")
        if action_command[0] == "Generate":
            break
        elif action_command[0] == "Contains":
            print(contains(action_command[1], raw_key))
        elif action_command[0] == "Flip":
            raw_key = flip(action_command[1], int(action_command[2]), int(action_command[3]), raw_key)
            print(raw_key)
        elif action_command[0] == "Slice":
            raw_key = remove_char(int(action_command[1]), int(action_command[2]), raw_key)
            print(raw_key)
    return raw_key

raw_activation_key = input()
print(f"Your activation key is: {main_action(raw_activation_key)}")
