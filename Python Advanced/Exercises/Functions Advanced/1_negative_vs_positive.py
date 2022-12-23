def sum_nums(*args):
    bigger_is_positive_sum = False
    positive_sum = sum([int(x) for x in args if int(x) > 0])
    negative_sum = sum([int(x) for x in args if int(x) < 0])
    if positive_sum > abs(negative_sum):
        bigger_is_positive_sum = True
    return f"{negative_sum}\n{positive_sum}", bigger_is_positive_sum

result = sum_nums(*input().split())
print(result[0])
print("The positives are stronger than the negatives" if result[1] else "The negatives are stronger than the positives")
