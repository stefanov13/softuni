def moving(way: str, teas_count: int, alice_position: tuple, game_over=False):
    r = alice_position[0] + movement[way][0]
    c = alice_position[1] + movement[way][1]

    if not (0 <= r < size and 0 <= c < size):
        game_over = True
        return game_over, teas_count, alice_position
    
    elif field[r][c] == "R":
        field[r][c] = "*"
        game_over = True
        return game_over, teas_count, alice_position
    
    elif field[r][c].isdigit():
        teas_count += int(field[r][c])
    
    alice_position = (r, c)
    field[r][c] = "*"    
    return game_over, teas_count, alice_position




size = int(input())
teas_found = 0
alice_current_position = tuple()
field = []
game_over = False

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = input().split()
    field.append(line)

    if "A" in line:
        alice_current_position = (row, line.index("A"))
        field[row][alice_current_position[1]] = "*"

while not game_over:
    direction = input()
    game_over, teas_found, alice_current_position = moving(direction, teas_found, alice_current_position)
    if teas_found >= 10:
        print("She did it! She went to the party.")
        break

else:
    print("Alice didn't make it to the tea party.")

for row in field:
    print(" ".join(row))
