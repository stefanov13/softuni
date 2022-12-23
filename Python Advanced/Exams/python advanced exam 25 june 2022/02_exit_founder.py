def determine_player(player_one, player_two, current_turn):
    player = (player_one if current_turn % 2 == 0 else player_two)
    other = (player_two if player == player_one else player_one)
    return player, other


player_1, player_2 = input().split(", ")

MAZE_SIZE = 6
current_player_turn = 0
drop_turn = {player_1: 0, player_2: 0}

maze_board = [input().split() for _ in range(MAZE_SIZE)]

while True:
    row, col = eval(input())
    current_player, other_player = determine_player(player_1, player_2, current_player_turn)
    if drop_turn[current_player] == 1:
        drop_turn[current_player] = 0
        current_player_turn += 1
        continue

    if maze_board[row][col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    
    elif maze_board[row][col] == "T":
        print(f"{current_player} is out of the game! The winner is {other_player}." )
        break

    elif maze_board[row][col] == "W":
        drop_turn[current_player] = 1
        print(f"{current_player} hits a wall and needs to rest.")
    
    current_player_turn += 1
