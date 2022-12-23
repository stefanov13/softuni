from collections import deque

petrol_pumps = deque()

petrol_pumps_count = int(input())


for _ in range(petrol_pumps_count):
    petrol_amount, distance = input().split()
    petrol_pumps.append([int(petrol_amount), int(distance)])

for attempt in range(petrol_pumps_count):
    current_petrol_amount = 0
    is_failed = False
    for fuel_quantity, distance_trip in petrol_pumps:
        current_petrol_amount += fuel_quantity

        if current_petrol_amount < distance_trip:
            is_failed = True
            break
        else:
            current_petrol_amount -= distance_trip

    if is_failed:
        petrol_pumps.append(petrol_pumps.popleft())
    else:
        print(attempt)
        break
