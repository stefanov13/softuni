def take_odd(password):
    result = ""
    for i, char in enumerate(password):
        if i % 2 != 0:
            result += char
    print(result)
    return result


def cut(start_pos, length, password):
    result = password[:start_pos] + password[start_pos + length:]
    print(result)
    return result


def substitute(part_for_replace, new_char, password):
    if part_for_replace in password:
        password = password.replace(part_for_replace, new_char)
        print(password)
        return password
    else:
        print("Nothing to replace!")
    return password


raw_password = input()
command = input()

while not command == "Done":
    action = command.split()[0]
    if action == "TakeOdd":
        raw_password = take_odd(raw_password)
    elif action == "Cut":
        start_index = command.split()[1]
        cut_length = command.split()[2]
        raw_password = cut(int(start_index), int(cut_length), raw_password)
    elif action == "Substitute":
        substring = command.split()[1]
        replacement_str = command.split()[2]
        raw_password = substitute(substring, replacement_str, raw_password)
    command = input()

print(f"Your password is: {raw_password}")
