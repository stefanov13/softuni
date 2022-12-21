nums_sequince = list(map(int, input().split()))
even_nums = list(filter(lambda x: x % 2 == 0, nums_sequince))
print(even_nums)
