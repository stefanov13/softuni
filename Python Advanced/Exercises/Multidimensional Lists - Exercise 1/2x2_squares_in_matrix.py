row, col = list(map(int, input().split()))
matrix = []

for _ in range(row):
    matrix.append([x for x in input().split()])

square_matrices_count = 0
for row_idx in range(row - 1):
    for col_idx in range(col - 1):
        current_element = matrix[row_idx][col_idx]
        if all(
            [current_element == matrix[row_idx][col_idx + 1],\
                 current_element == matrix[row_idx + 1][col_idx],\
                    current_element == matrix[row_idx + 1][col_idx + 1]]
        ):
            square_matrices_count += 1

print(square_matrices_count)
