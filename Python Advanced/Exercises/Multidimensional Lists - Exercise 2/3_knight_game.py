size = int(input())
chess_matrix = [list(input()) for _ in range(size)]

movement = (
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    pos_of_max_attacks_knight = []

    for row in range(size):
        for col in range(size):
            if chess_matrix[row][col] == "K":
                attacks = 0
                for pos in movement:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if chess_matrix[pos_row][pos_col] == "K":
                            attacks += 1
                if attacks > max_attacks:
                    pos_of_max_attacks_knight = [row, col]
                    max_attacks = attacks
    if pos_of_max_attacks_knight:
        chess_matrix[pos_of_max_attacks_knight[0]][pos_of_max_attacks_knight[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
