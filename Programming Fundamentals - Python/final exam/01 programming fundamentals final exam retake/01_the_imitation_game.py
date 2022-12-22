def moves_first_letters(char_count, message):
    part_for_movie = message[:char_count]
    rest_char = message[char_count:]
    result_message = rest_char + part_for_movie
    return result_message


def inserts_value(index_to_add, value_to_add, message):
    first_part = message[:index_to_add]
    last_part = message[index_to_add:]
    result_message = first_part + value_to_add + last_part
    return result_message


def changes_occurrences(chars_for_replace, new_chars, message):
    result_message = ""
    for letter in message:
        if letter == chars_for_replace:
            result_message += new_chars
        else:
            result_message += letter
    return result_message


message_for_decrypting = input()
action_command = input()

while not action_command == "Decode":
    if action_command.split("|")[0] == "Move":
        letters_count = int(action_command.split("|")[1])
        message_for_decrypting = moves_first_letters(letters_count, message_for_decrypting)
    elif action_command.split("|")[0] == "Insert":
        insert_index = int(action_command.split("|")[1])
        value_for_insert = action_command.split("|")[2]
        message_for_decrypting = inserts_value(insert_index, value_for_insert, message_for_decrypting)
    elif action_command.split("|")[0] == "ChangeAll":
        old_char = action_command.split("|")[1]
        new_char = action_command.split("|")[2]
        message_for_decrypting = changes_occurrences(old_char, new_char, message_for_decrypting)

    action_command = input()

print(f"The decrypted message is: {message_for_decrypting}")
