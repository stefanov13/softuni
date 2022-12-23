def santas_pos(neighborhood: list):
    for row_i, row in enumerate(neighborhood):
        for col_i, col in enumerate(row):
            if col == "S":
                neighborhood[row_i][col_i] = "-"
                return (row_i, col_i), neighborhood


def check_current_positions(row: int, col: int, count_of_presents: int, nice_kids_count: int, neighborhood: list):
    santas_current_position = (row, col)
    if neighborhood[row][col] == "V":
        neighborhood[row][col] = "-"
        count_of_presents -= 1
        nice_kids_count -= 1
    elif neighborhood[row][col] == "C":
        if 0 < row and count_of_presents > 0 and neighborhood[row-1][col] in ("V", "X"):
            if neighborhood[row-1][col] == "V":
                nice_kids_count -= 1
            neighborhood[row-1][col] = "-"
            count_of_presents -= 1
        if row < len(neighborhood) - 1 and count_of_presents > 0 and neighborhood[row+1][col] in ("V", "X"):
            if neighborhood[row+1][col] == "V":
               nice_kids_count -= 1 
            neighborhood[row+1][col] = "-"
            count_of_presents -= 1
        if 0 < col and count_of_presents > 0 and neighborhood[row][col-1] in ("V", "X"):
            if neighborhood[row][col-1] == "V":
                nice_kids_count -= 1
            neighborhood[row][col-1] = "-"
            count_of_presents -= 1
        if col < len(neighborhood) -1 and count_of_presents > 0 and neighborhood[row][col+1] in ("V", "X"):
            if neighborhood[row][col+1] == "V":
                nice_kids_count -= 1
            neighborhood[row][col+1] = "-"
            count_of_presents -= 1
    else:
        neighborhood[row][col] = "-"
    return neighborhood, santas_current_position, nice_kids_count, count_of_presents
        



presents_count = int(input())
neighborhood_size = int(input())

neighborhood_matrix = []
nice_kids = 0
for _ in range(neighborhood_size):
    neighborhood_matrix.append(input().split())
    nice_kids += (neighborhood_matrix[-1]).count("V")
nice_kids_left = nice_kids

santas_presents = presents_count
santas_position, neighborhood_matrix = santas_pos(neighborhood_matrix)

while True:
    command_type = input()

    if command_type == "Christmas morning":
        break

    if command_type == "up" and 0 < santas_position[0]:
        neighborhood_matrix, santas_position, nice_kids_left, santas_presents = check_current_positions(santas_position[0] - 1, santas_position[1], santas_presents, nice_kids_left, neighborhood_matrix)

    elif command_type == "down" and santas_position[0] < neighborhood_size - 1:
        neighborhood_matrix, santas_position, nice_kids_left, santas_presents = check_current_positions(santas_position[0] + 1, santas_position[1], santas_presents, nice_kids_left, neighborhood_matrix)

    elif command_type == "left" and 0 < santas_position[1]:
        neighborhood_matrix, santas_position, nice_kids_left, santas_presents = check_current_positions(santas_position[0], santas_position[1] - 1, santas_presents, nice_kids_left, neighborhood_matrix)

    elif command_type == "right" and santas_position[1] < neighborhood_size - 1:
        neighborhood_matrix, santas_position, nice_kids_left, santas_presents = check_current_positions(santas_position[0], santas_position[1] + 1, santas_presents, nice_kids_left, neighborhood_matrix)
    
    if santas_presents < 1:
        break

neighborhood_matrix[santas_position[0]][santas_position[1]] = "S"

if not santas_presents and nice_kids_left:
    print("Santa ran out of presents!")

[print(f"{' '.join(el)}") for el in neighborhood_matrix]

if not nice_kids_left:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")
