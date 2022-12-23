def age_assignment(*args, **kwargs):
    result_dict = {name:kwargs[name[0]] for name in args if name[0] in kwargs}        
    sorted_result = dict(sorted(result_dict.items()))
    result_ = ""
    for key, val in sorted_result.items():
        result_ += f"{key} is {val} years old." + "\n"
    return result_


# def get_name(names: tuple, letter: str):
#     for name in names:
#         if name.startswith(letter):
#             return name


# def age_assignment(*args, **kwargs):
#     people = {}
#     result_ = ""
#     for key, val in kwargs.items():
#         name = get_name(args, key)
#         people[name] = val
#     sorted_result = dict(sorted(people.items()))

#     for name, age in sorted_result.items():
#         result_ += f"{name} is {age} years old.\n"
#     return result_


# Next lines not submit in judge system!
print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
