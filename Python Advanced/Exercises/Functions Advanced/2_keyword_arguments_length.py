def kwargs_length(**kwarg):
    return len(kwarg)

# Next lines not submit in judge system!

dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
