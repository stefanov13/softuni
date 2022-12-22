import re

my_pattern = r"\d+"
result = []

while True:
    given_string = input()
    if not given_string:
        break

    finded_result = re.findall(my_pattern, given_string)
    if len(finded_result) > 0:
        result += finded_result

print(" ".join(result))
