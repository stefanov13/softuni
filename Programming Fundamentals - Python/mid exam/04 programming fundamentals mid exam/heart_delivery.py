neighborhood = [int(i) for i in input().split("@")]

jump_length = input()

current_position = 0

while jump_length not in "Love!":
    position = int(jump_length.split()[1]) + current_position
    if position >= len(neighborhood):
        if neighborhood[0] > 0:
            neighborhood[0] -= 2
            if neighborhood[0] == 0:
                print("Place 0 has Valentine's day.")
        else:
            print("Place 0 already had Valentine's day.")
        current_position = 0
    else:
        if neighborhood[position] > 0:
            neighborhood[position] -= 2
            if neighborhood[position] == 0:
                print(f"Place {position} has Valentine's day.")
        else:
            print(f"Place {position} already had Valentine's day.")
        current_position = position


    jump_length = input()

failed_places = len([i for i in neighborhood if i > 0])
    

print(f"Cupid's last position was {current_position}.")
if failed_places == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {failed_places} places.")
