from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = input()

index_snake = 0

for row in range(rows):
    snake_matrix = deque()
    for col in range(cols):
        if index_snake == len(snake):
            index_snake = 0
        if row % 2 == 0:
            snake_matrix.append(snake[index_snake])
        else:
            snake_matrix.appendleft(snake[index_snake])
        index_snake += 1
    print("".join(snake_matrix))
