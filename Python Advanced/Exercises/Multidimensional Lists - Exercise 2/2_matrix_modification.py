def is_valid_coordinates(row: int, col: int, size: int):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def action(command: str, row: int, col: int, value: int, size: int, matrix: list):
    valid_coordinates = is_valid_coordinates(row, col, size)
    if not valid_coordinates:
        print("Invalid coordinates")
    elif command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value
    
    return matrix


size = int(input())

matrix = [[int(x) for x in (input().split())] for _ in range(size)]

manipulation = input()

while not manipulation == "END":
    action_, row, col, value = manipulation.split()
    matrix = action(action_, int(row), int(col), int(value), size, matrix)
    manipulation = input()

for row in matrix:
    print(*row)
