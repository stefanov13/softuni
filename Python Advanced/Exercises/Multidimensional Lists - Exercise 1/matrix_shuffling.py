rows, cols = tuple(map(int, input().split()))
matrix = [input().split() for _ in range(rows)]



while True:
    command = input().split()
    if command[0] == "END":
        break
    
    if "swap" not in command or not len(command) == 5:
        print("Invalid input!")
        continue
    
    points = list(map(int, command[1:]))
    if False in [
        0 <= points[0] < rows,
        0 <= points[1] < cols,
        0 <= points[2] < rows,
        0 <= points[3] < cols
        ]:
        print("Invalid input!")
        continue
        
    p1, p2 = matrix[points[0]][points[1]], matrix[points[2]][points[3]]
    matrix[points[0]][points[1]] = p2
    matrix[points[2]][points[3]] = p1
    
    for row in matrix:
        print(*row)
