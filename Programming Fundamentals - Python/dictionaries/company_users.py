companys_name = {}

company = input().split(" -> ")

while not company[0] in "End":
    if not company[0] in companys_name:
        companys_name[company[0]] = [company[1]]
    else:
        employees = companys_name[company[0]]
        if not company[1] in employees:
            employees.append(company[1])
        companys_name[company[0]] = employees

    company = input().split(" -> ")

for k, v in companys_name.items():
    print(f"{k}")
    for identification in v:
        print(f"-- {identification}")
