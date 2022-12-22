def insert_space(index_to_add, text):
    first_part = text[:index_to_add]
    last_part = text[index_to_add:]
    result_text = first_part + chr(32) + last_part
    print(result_text)
    return result_text


def reverse(part_of_string, text):
    if part_of_string in text:
        index_find_text = text.find(part_of_string)
        text = text[:index_find_text] + text[index_find_text + (len(part_of_string)):]
        text += part_of_string[::-1]
        print(text)
        return text
    print("error")
    return text


def change_all(part_of_str, new_str, text):
    while part_of_str in text:
        text = text.replace(part_of_str, new_str)
    print(text)
    return text


message = input()
operation_command = input()

while not operation_command == "Reveal":
    if operation_command.split(":|:")[0] == "InsertSpace":
        index_for_insert = int(operation_command.split(":|:")[1])
        message = insert_space(index_for_insert, message)
    elif operation_command.split(":|:")[0] == "Reverse":
        substring = operation_command.split(":|:")[1]
        message = reverse(substring, message)
    elif operation_command.split(":|:")[0] == "ChangeAll":
        substr = operation_command.split(":|:")[1]
        replacement = operation_command.split(":|:")[2]
        message = change_all(substr, replacement, message)

    operation_command = input()

print(f"You have a new text message: {message}")
