scores = int(input())
bonus_points = 0
even = 0
five_end = 0

if scores <= 100 :
    bonus_points = 5
elif scores > 1000 :
    bonus_points = scores * 0.1
else :
    bonus_points = scores * 0.2


if scores % 2 == 0 :
    even = 1

if scores % 10 == 5 :
    five_end = 2

sum_bonus_points = bonus_points + even + five_end
sum_points = scores + bonus_points + even + five_end

print (sum_bonus_points)
print (sum_points)
