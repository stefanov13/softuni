def perfect_num_check(checking_num):
    if checking_num in (6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176, 191561942608236107294793378084303638130997321548169216):
        perfect_num = "We have a perfect number!"
    else:
        perfect_num = "It's not so perfect."
    return(perfect_num)

num = int(input())

print(perfect_num_check(num))
