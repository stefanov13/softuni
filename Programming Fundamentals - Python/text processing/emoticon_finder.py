sentence = input()
finded_emoticons = [sentence[i]+sentence[i+1] for i in range(len(sentence)) if sentence[i] == ":"]

print("\n".join(finded_emoticons))
