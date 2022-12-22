import re

my_pattern = r"\b_([a-zA-Z0-9]+\b)"

text = input()
match_char = re.findall(my_pattern, text)
print(",".join(match_char))
