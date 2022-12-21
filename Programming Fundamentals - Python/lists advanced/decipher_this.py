import re

code_str = input()
splited_str = re.split("(\d+)", code_str)
splited_str = [i for i in splited_str if i]

clean_str = []
for i in splited_str:
    clean_str.append(i.strip())
decode_value = [chr(int(j)) for i, j in enumerate(clean_str) if i % 2 == 0]
decode_str = [j for i, j in enumerate(clean_str) if i % 2 != 0]
result_list = []
for dechipher_word in decode_str:
    if len(dechipher_word) > 1:
        result_list.append(dechipher_word[-1:] + dechipher_word[1:-1] + dechipher_word[:1])
    else:
        result_list.append(dechipher_word)

result = [None]*(len(decode_value)+len(result_list))
result[::2] = decode_value
result[1::2] = result_list
con_word = []

con_word = [result[i] + result[i+1] for i in range(0, len(result), 2)]

print(" ".join(con_word))
