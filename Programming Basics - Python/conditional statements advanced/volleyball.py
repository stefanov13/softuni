from math import floor

year_type = input()
holydays = int(input())
born_city_weekends = int(input())

sofia_weekends = 48 - born_city_weekends
weekends_playing = sofia_weekends * (3 / 4)
holydays_playing = holydays * (2 / 3)
all_play = weekends_playing + holydays_playing + born_city_weekends

if year_type == "leap":
    all_play *= 1.15

print(floor(all_play))
