row_col_count = int(input())
matrix = []

for _ in range(row_col_count):
    matrix.append([int(x) for x in input().split()])


primary_diagonal = 0
for row_idx in range(len(matrix)):
    primary_diagonal += matrix[row_idx][row_idx]

secondary_diagonal = 0
row_idx = 0
for col_idx in range(len(matrix) - 1, -1, -1):
    secondary_diagonal += matrix[row_idx][col_idx]
    row_idx += 1

print(abs(primary_diagonal - secondary_diagonal))
