contacts = {}

while True:
    contact = input().split("-")
    if contact[0].isdigit():
        search_count = int(contact[0])
        break
    contacts[contact[0]] = contact[1]

for _ in range(search_count):
    name = input()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print(f"Contact {name} does not exist.")
