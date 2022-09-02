hour = int(input())
minutes  = int(input())

minutes = minutes + 15

if minutes >= 60:
    minutes = minutes - 60
    hour = hour + 1

if hour == 24:
    hour = 0

print (f"{hour}:{minutes:02d}")
