number_of_strings = int(input())

for _ in range(number_of_strings):
    given_string = input()
    if "," in given_string:
        print(f"{given_string} is not pure!")
    elif "." in given_string:
        print(f"{given_string} is not pure!")
    elif "_" in given_string:
        print(f"{given_string} is not pure!")
    else:
        print(f"{given_string} is pure.")
