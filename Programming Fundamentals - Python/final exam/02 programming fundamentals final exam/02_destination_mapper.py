import re
place_on_map = input()

pattern = re.compile(r"(=|/)([A-Z][A-Za-z]{2,})\1")
travel_points = 0

finded_places = [m.group(2) for m in re.finditer(pattern, place_on_map)]
for el in finded_places:
    travel_points += len(el)

print(f"Destinations: {', '.join(finded_places)}")
print(f"Travel Points: {travel_points}")
