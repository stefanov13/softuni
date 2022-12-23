def even_odd_filter(**kwargs):
    result_dict = {}
    for k, v in kwargs.items():
        if k == "even":
            result_dict[k] = [int(x) for x in v if int(x) % 2 == 0]
        else:
            result_dict[k] = [int(x) for x in v if int(x) % 2 != 0]
    return dict(sorted(result_dict.items(), key=lambda x: -(len(x[1]))))
    

# Next lines not submit in judge system!
print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
