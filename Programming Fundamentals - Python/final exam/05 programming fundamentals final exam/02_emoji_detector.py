import re

pattern = r"([0-9])|(\:{2}[A-Z][a-z]{2,}\:{2})|(\*{2}[A-Z][a-z]{2,}\*{2})"

text = input()
cool_threshold = 1
all_emojis = []

all_matches = re.finditer(pattern, text)
if all_matches:
    for match in all_matches:
        if (match.group()).isdigit():
            cool_threshold *= int(match.group())
        else:
            emoji_ord = [ord(letter) for letter in match.group() if letter.isalpha()]
            emoji_sum = sum(emoji_ord)
            all_emojis.append([match.group(), emoji_sum])

print(f"Cool threshold: {cool_threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
for emoji in all_emojis:
    if emoji[1] > cool_threshold:
        print(emoji[0])
