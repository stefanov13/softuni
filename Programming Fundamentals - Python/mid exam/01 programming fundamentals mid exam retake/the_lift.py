people_count = int(input())
lift_state = list(map(int, input().split()))

for cabin in range(len(lift_state)):
    for seat in range(lift_state[cabin], 4):
        if people_count > 0:
            lift_state[cabin] += 1
            people_count -= 1
        else:
            break

all_seats = len(lift_state) * 4
used_seats = sum(lift_state)
cabins = " ".join(map(str, lift_state))
if people_count == 0 and used_seats < all_seats:
    print("The lift has empty spots!")
elif people_count > 0:
    print(f"There isn't enough space! {people_count} people in a queue!")
print(cabins)
