import re

text = input()

pattern = r"(#|@)(([A-Za-z]{3,})\1{2}([A-Za-z]{3,}))\1"

matches = [[el.group(3), el.group(4)] for el in re.finditer(pattern, text)]
result = [valid for valid in matches if valid[1] == valid[0][::-1]]

if matches:        
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

if result:
    print("The mirror words are:")
    for i, res in enumerate(result):
        if i == len(result) - 1:
            print(f"{res[0]} <=> {res[1]}")
        else:
            print(f"{res[0]} <=> {res[1]}", end=", ")
else:
    print("No mirror words!")
