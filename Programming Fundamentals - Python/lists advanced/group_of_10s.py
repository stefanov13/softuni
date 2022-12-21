num = list(map(int, input().split(", ")))
  
if max(num) % 10 == 0:
    max_group = max(num) // 10
else:
    max_group = (max(num) // 10) + 1
    
filtered_num = [[]] * max_group

for group in range(max_group):
    filtered_num[group] = list(filter(lambda number: number <= (group + 1) * 10, num))
    for ready in filtered_num[group]:
        num.remove(ready)
                 
for i in range(max_group):
    print(f"Group of {(i + 1) * 10}'s: {filtered_num[i]}")
