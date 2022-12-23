def even_odd(*args):
    command_type = args[-1]
    if command_type == "even":
        result = [int(args[i]) for i in range(len(args)-1) if int(args[i]) % 2 == 0]
    else:
        result = [int(args[i]) for i in range(len(args)-1) if int(args[i]) % 2 != 0]
    return result


# Next lines not submit in judge system!
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
