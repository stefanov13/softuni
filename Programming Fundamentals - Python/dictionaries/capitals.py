countrys = input().split(", ")
capitals = input().split(", ")

country_capytals = zip(countrys, capitals)
country_capytals = dict(country_capytals)

for country, capital in country_capytals.items():
    print(f"{country} -> {capital}")
