row, col = list(map(int, input().split()))
matrix = []

for _ in range(row):
    matrix.append([int(x) for x in input().split()])

maximum_sum  = -999999999999999999999
result_matrix = []
for row_idx in range(row - 2):
    for col_idx in range(col - 2):
        checked_first_row = [matrix[row_idx][col_idx], matrix[row_idx][col_idx + 1], matrix[row_idx][col_idx + 2]]
        checked_second_row = [matrix[row_idx + 1][col_idx], matrix[row_idx + 1][col_idx + 1], matrix[row_idx + 1][col_idx + 2]]
        checked_third_row = [matrix[row_idx + 2][col_idx], matrix[row_idx + 2][col_idx + 1], matrix[row_idx + 2][col_idx + 2]]
        current_sum = sum(checked_first_row) + sum(checked_second_row) + sum(checked_third_row)
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            result_matrix = []
            result_matrix.append(checked_first_row)
            result_matrix.append(checked_second_row)
            result_matrix.append(checked_third_row)


print(f"Sum = {maximum_sum}")
for el in result_matrix:
    print(*el)
