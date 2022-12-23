symbols_for_replace = ["-", ",", ".", "!", "?"]

with open("01_even_lines/text.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):
    for symbol in symbols_for_replace:
        text[row] = text[row].replace(symbol, "@")

    print(*text[row].split()[::-1], sep=" ")
