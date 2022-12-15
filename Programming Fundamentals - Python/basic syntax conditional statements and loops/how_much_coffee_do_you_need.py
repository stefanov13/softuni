task = input()
coffee_caps_needed = 0

while task not in "END":
    if task.isupper() and task.lower() in ("coding", "dog", "cat", "movie"):
        coffee_caps_needed += 2
    elif task.islower() and task.lower() in ("coding", "dog", "cat", "movie"):
        coffee_caps_needed += 1
    
    task = input()

if coffee_caps_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_caps_needed)
