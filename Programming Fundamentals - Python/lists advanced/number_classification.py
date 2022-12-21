def positive_num(numbers):
    posituve_result = [pos_nums for pos_nums in numbers if pos_nums >= 0]
    return posituve_result


def negative_num(numbers):
    negative_result = [neg_nums for neg_nums in numbers if neg_nums < 0]
    return negative_result


def even_num(numbers):
    even_result = [even_nums for even_nums in numbers if even_nums % 2 == 0]
    return even_result


def odd_num(numbers):
    odd_result = [odd_nums for odd_nums in numbers if odd_nums % 2 != 0]
    return odd_result


numbers = list(map(int, input().split(", ")))

print("Positive: ", end="")
print(", ".join(map(str, positive_num(numbers))))
print("Negative: ", end="")
print(", ".join(map(str, negative_num(numbers))))
print("Even: ", end="")
print(", ".join(map(str, even_num(numbers))))
print("Odd: ", end="")
print(", ".join(map(str, odd_num(numbers))))
