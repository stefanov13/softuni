exam_hour = int(input())
exam_minutes = int(input())
arive_hour = int(input())
arive_minutes = int(input())

exam_time = (exam_hour * 60) + exam_minutes
arive_time = (arive_hour * 60) + arive_minutes

time_before = 0
time_after = 0


if exam_time >= arive_time:
    time_before = exam_time - arive_time
elif arive_time > exam_time:
    time_after = arive_time - exam_time

hour_before = (time_before // 60)
minutes_before = (time_before % 60)
hour_after = (time_after // 60)
minutes_after = (time_after % 60)

if 1 <= time_before <= 30 :
    print("On time")
elif exam_time == arive_time:
    print("On time")
elif time_before > 30:
    print("Early")
else:
    print("Late")

if 1 <= time_before <= 59:
    print(f"{minutes_before} minutes before the start")
elif time_before >= 60:
    print(f"{hour_before}:{minutes_before:02d} hours before the start")

if 1<= time_after <= 59:
    print(f"{minutes_after} minutes after the start")
elif time_after >= 60:
    print(f"{hour_after}:{minutes_after:02d} hours after the start")
