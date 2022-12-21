def check_len(password):
    return 6 <= len(password) <= 10


def check_num(password):
    nums_count = 0
    for symbol in password:
        if symbol.isdigit():
            nums_count += 1
    return nums_count


def check_special(password):
    special_count = 0
    for symbol in password:
        if ord(symbol) in range(48, 58) or ord(symbol)\
             in range(65, 91) or ord(symbol) in range(97, 123):
            special_count += 1
        else:
            special_count -= 1
    return special_count


entered_password = input()

if not check_len(entered_password):
    print("Password must be between 6 and 10 characters")

if check_special(entered_password) is not len(entered_password):
    print("Password must consist only of letters and digits")    

if check_num(entered_password) < 2:
    print("Password must have at least 2 digits")

if check_len(entered_password) and check_num(entered_password) >= 2\
     and check_special(entered_password) is len(entered_password):
    print("Password is valid")
