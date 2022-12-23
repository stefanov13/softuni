def check_direction(way: str, pos: tuple, best_collected_eggs: int):
    collected_eggs = 0
    current_path = []
    r = bunny_current_position[0] + pos[0]
    c = bunny_current_position[1] + pos[1]

    while 0 <= r < len(field) and 0 <= c < len(field):
        if field[r][c] == "X":
            break
        else:
            collected_eggs += int(field[r][c])
            current_path.append([r, c])

        r += pos[0]
        c += pos[1]

    if collected_eggs >= best_collected_eggs:
        return way, collected_eggs, current_path

    return best_collected_eggs


size = int(input())
field = []
best_path = []
best_way = ""
best_collected_eggs = 0

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = input().split()
    field.append(line)

    if "B" in line:
        bunny_current_position = (row, line.index("B"))

for direction, coordinates in movement.items():
    best_collected_eggs = check_direction(direction, coordinates, best_collected_eggs)
    is_int = isinstance(best_collected_eggs, int)

    if not is_int:
        best_way = best_collected_eggs[0]
        best_path = best_collected_eggs[2]
        best_collected_eggs = best_collected_eggs[1]
        
print(best_way)
for pos in best_path:
    print(pos)
print(best_collected_eggs)
