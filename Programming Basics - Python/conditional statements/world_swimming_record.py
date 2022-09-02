from math import floor

record = float(input())
distance = float(input())
swimming_time_1m_distance = float(input())


target_distance = distance * swimming_time_1m_distance
delayed_counts = distance / 15
delayed_time = floor(delayed_counts) * 12.5
full_time = target_distance + delayed_time

if record < full_time:
    shortage_time = full_time - record
    print (f"No, he failed! He was {shortage_time:.2f} seconds slower.")
else:
    print (f"Yes, he succeeded! The new world record is {full_time:.2f} seconds.")
