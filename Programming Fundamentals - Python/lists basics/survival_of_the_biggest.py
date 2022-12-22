entry_value_nums = list(map(int, input().split()))
count_must_remove = int(input())

for _ in range(count_must_remove):
    min1 = entry_value_nums[0]
    for value in entry_value_nums:
        if value < min1:
            min1 = value
    entry_value_nums.remove(min1)    

print(', '.join(map(str, entry_value_nums)))
