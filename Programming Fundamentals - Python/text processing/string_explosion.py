strength = input().split(">")
strength_explosions = [0] * len(strength)

for i, el in enumerate(strength):
    with_symbol = ">"
    if el[0].isdigit():
        with_symbol += el
        strength[i] = with_symbol
        strength_explosions[i] = int(el[0])

for i, v in enumerate(strength):
    if v.startswith(">") and len(v) - 1 >= strength_explosions[i]:
        strength[i] = v[0] + v[strength_explosions[i]+1:]
    elif v.startswith(">"):
        if len(strength)-1 == i and strength_explosions[-1] > len(v):
            strength[i] = v[0]
            continue
        strength[i] = v[0]
        strength_explosions[i+1] += strength_explosions[i] - (len(v) - 1) 
print("".join(strength))
