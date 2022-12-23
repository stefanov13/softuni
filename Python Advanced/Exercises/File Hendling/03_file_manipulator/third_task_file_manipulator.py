import os

while True:
    data = input().split("-")

    if data[0] == "Create":
        file = open(f"03_file_manipulator/{data[1]}", "w")
        file.close()

    elif data[0] == "Add":
        with open(f"03_file_manipulator/{data[1]}", "a") as file:
            file.write(f"{data[2]}\n")

    elif data[0] == "Replace":
        try:
            with open(f"03_file_manipulator/{data[1]}", "r+") as file:
                text = file.readlines()
            file = open(f"03_file_manipulator/{data[1]}", "w")

            for i in range(len(text)):
                text[i] = text[i].replace(data[2], data[3])
            
            file.write(''.join(text))
            file.close()
        except FileNotFoundError:
            print("An error occurred")

    elif data[0] == "Delete":
        try:
            os.remove(f"03_file_manipulator/{data[1]}")
        except:
            print("An error occurred")
    
    else:
        break
