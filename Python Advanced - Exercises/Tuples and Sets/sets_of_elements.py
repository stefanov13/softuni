first_set_len, second_set_len = list(map(int, input().split()))

first_set = set()
second_set = set()

for _ in range(first_set_len):
    first_set.add(int(input()))

for _ in range(second_set_len):
    second_set.add(int(input()))

result_ = first_set.intersection(second_set)

for num in result_:
    print(num)
