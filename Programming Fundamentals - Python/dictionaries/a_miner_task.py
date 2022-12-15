resources = {}

while True:
    ore = input()
    if ore == "stop":
        break
    quantity = int(input())
    if ore in resources:
        resources[ore] += quantity
    else:
        resources[ore] = quantity
        

for key, values in resources.items():
    print(f"{key} -> {values}")
