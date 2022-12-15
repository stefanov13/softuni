def check_age(drinker_age):
    if drinker_age <= 14:
        return "drink toddy"
    elif 15 <= drinker_age <= 18:
        return "drink coke"
    elif 19 <= drinker_age <= 21:
        return "drink beer"
    else:
        return "drink whisky"

age = int(input())
print(check_age(age))
