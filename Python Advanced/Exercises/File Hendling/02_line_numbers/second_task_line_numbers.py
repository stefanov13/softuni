from string import punctuation

output_file = open("02_line_numbers/output.txt", "a")

with open("02_line_numbers/text.txt", "r") as text_file:
    text = text_file.readlines()

for i in range(len(text)):
    row = text[i]

    marks = 0
    letters = 0

    for symbol in row:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i+1}: {''.join(row[:-1])} ({letters}) ({marks})\n")
    
output_file.close()
