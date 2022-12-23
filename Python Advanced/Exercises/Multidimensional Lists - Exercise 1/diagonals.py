row_col_count = int(input())
matrix = []

for _ in range(row_col_count):
    matrix.append([int(x) for x in input().split(", ")])


primary_diagonal = []
for row_idx in range(len(matrix)):
    primary_diagonal.append(matrix[row_idx][row_idx])

secondary_diagonal = []
row_idx = 0
for col_idx in range(len(matrix) - 1, -1, -1):
    secondary_diagonal.append(matrix[row_idx][col_idx])
    row_idx += 1

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
