num_of_rooms = int(input())

free_chairs = 0
needed_chairs = None

for rooms in range(num_of_rooms):
    chairs_and_visitors = input().split(" ")
    if len(chairs_and_visitors[0]) >= int(chairs_and_visitors[1]):
        free_chairs  += len(chairs_and_visitors[0]) - int(chairs_and_visitors[1])
    else:
        needed_chairs = int(chairs_and_visitors[1]) - len(chairs_and_visitors[0])
        print(f"{needed_chairs} more chairs needed in room {rooms + 1}")

if needed_chairs is None:
    print(f"Game On, {free_chairs} free chairs left")
