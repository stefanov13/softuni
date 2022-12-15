operation_count = int(input())

visitors = {}

for _ in range(operation_count):
    operation = input().split()
    if operation[0] == "register":
        if not operation[1] in visitors:
            visitors[operation[1]] = operation[2]
            print(f"{operation[1]} registered {operation[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {operation[2]}")
    elif operation[0] == "unregister":
        if operation[1] in visitors:
            visitors.pop(operation[1])
            print(f"{operation[1]} unregistered successfully")
        else:
            print(f"ERROR: user {operation[1]} not found")

for k, v in visitors.items():
    print(f"{k} => {v}")
