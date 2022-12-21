def smallest_of_tree_int(numbers):
    return min(numbers)


three_num = [int(input()) for _ in range(3)]

print(smallest_of_tree_int(three_num))

# def smallest_of_tree_int(a, b, c):
#     if a > b > c:
#         return(c)
#     elif a > b < c:
#         return(b)
#     elif b > a < c:
#         return(a)


# a = int(input())
# b = int(input())
# c = int(input())

# print(smallest_of_tree_int(a, b, c))
