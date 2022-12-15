word = input()


while word not in "End":
    repeated_word = ""
    if word in "SoftUni":
        word = input()
        continue
    for letter in word:
        repeated_word += (letter + letter)
    print(repeated_word)
    word = input()
