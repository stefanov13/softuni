players_card = input().split()
players_card = set(players_card)

A_TEAM_COUNT = 11
B_TEAM_COUNT = 11
game_stoped = False

for element in players_card:
    if "A" in element:
        A_TEAM_COUNT -= 1
    else:
        B_TEAM_COUNT -= 1
    if A_TEAM_COUNT == 6 or B_TEAM_COUNT == 6:
        game_stoped = True
        break

print(f"Team A - {A_TEAM_COUNT}; Team B - {B_TEAM_COUNT}")
if game_stoped:
    print("Game was terminated")
