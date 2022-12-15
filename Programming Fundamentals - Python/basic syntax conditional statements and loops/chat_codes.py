def chat_decoder(chat_code):
    if chat_code == 88:
        return "Hello"
    elif chat_code == 86:
        return "How are you?"
    elif chat_code <= 87:
        return "GREAT!"
    else:
        return "Bye."

num_of_message = int(input())

for _ in range(num_of_message):
    code = int(input())
    print(chat_decoder(code))
