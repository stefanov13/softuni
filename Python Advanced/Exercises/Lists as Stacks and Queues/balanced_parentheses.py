expression = input()

par_stack = []
is_used = True

for index in range(len(expression)):
    current_symbol = expression[index]
    if current_symbol == "(" or current_symbol == "{" or current_symbol == "[":
        par_stack.append(current_symbol)
    elif not par_stack:
        is_used = False
        break
    elif current_symbol == ")":
        if par_stack[-1] == "(":
            par_stack.pop()
    elif current_symbol == "}":
        if par_stack[-1] == "{":
            par_stack.pop()
    elif current_symbol == "]":
        if par_stack[-1] == "[":
            par_stack.pop()

if not par_stack and is_used:
    print("YES")
else:
    print("NO")
