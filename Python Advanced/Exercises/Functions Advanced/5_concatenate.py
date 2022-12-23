def concatenate(*args, **kwargs):
    result_str = ""
    for text in args:
        result_str += text
    for k, v in kwargs.items():
        if k in result_str:
            result_str = result_str.replace(k, v)
    return result_str

# Next lines not submit in judge system!
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
