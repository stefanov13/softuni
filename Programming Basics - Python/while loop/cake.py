wide = int(input())
length = int(input())

count_all_pieces = wide * length
pieces_left = count_all_pieces


while pieces_left >= 0:
    pieces_taken = input()

    if pieces_taken == "STOP":
        print(f"{pieces_left} pieces are left.")
        break

    pieces_left -= int(pieces_taken)

if pieces_left < 0:
    print(f"No more cake left! You need {abs(pieces_left)} pieces more.")
