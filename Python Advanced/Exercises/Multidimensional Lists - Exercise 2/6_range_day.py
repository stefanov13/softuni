def moving(way: str, steps: int):
    r = current_position[0] + (movement[way][0] * steps)
    c = current_position[1] + (movement[way][1] * steps)

    if not (0 <= r < SHOTGUN_RANGE_SIZE and 0 <= c < SHOTGUN_RANGE_SIZE):
        return current_position

    if shotgun_range[r][c] == "x":
        return current_position

    return r, c

def shoot(way: str):
    r = current_position[0] + movement[way][0]
    c = current_position[1] + movement[way][1]

    while (0 <= r < SHOTGUN_RANGE_SIZE and 0 <= c < SHOTGUN_RANGE_SIZE):       
        if shotgun_range[r][c] == "x":
            shotgun_range[r][c] = "."

            return r, c
        
        r += movement[way][0]
        c += movement[way][1]

        
SHOTGUN_RANGE_SIZE = 5
targets_count = 0
positions_hit_targets = []
current_position = tuple()
shotgun_range = []

movement = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


for row in range(SHOTGUN_RANGE_SIZE):
    line = input().split()
    shotgun_range.append(line)

    if "A" in line:
        current_position = (row, line.index("A"))
        shotgun_range[row][current_position[1]] = "."
    
    targets_count += line.count("x")
    

command_count = int(input())

for shot in range(command_count):
    command_ = input().split()

    if command_[0] == "move":
        current_position = moving(command_[1], int(command_[2]))
    elif command_[0] == "shoot":
        hit_tarrget = shoot(command_[1])
        
        if hit_tarrget:
            positions_hit_targets.append([hit_tarrget[0], hit_tarrget[1]])

        if len(positions_hit_targets) == targets_count:
            print(f"Training completed! All {targets_count} targets hit.")
            break

if len(positions_hit_targets) < targets_count:
    print(f"Training not completed! {targets_count - len(positions_hit_targets)} targets left.")

[print(down_target) for down_target in positions_hit_targets]
