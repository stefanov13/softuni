count_of_lines = int(input())

unique_elements = set()
for _ in range(count_of_lines):
    elements = input().split()
    element_ = [unique_elements.add(el) for el in elements]

print('\n'.join(unique_elements))
