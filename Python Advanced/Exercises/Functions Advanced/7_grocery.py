def grocery_store(**kwargs):
    sorted_result = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result_ = ""
    for key, val in sorted_result.items():
        result_ += f"{key}: {val}"+"\n"
    return result_


# Next lines not submit in judge system!
print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
