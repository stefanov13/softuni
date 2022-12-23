from posixpath import split


n = int(input())

longest_intersection = set()
for _ in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")
    first_num_range = set(range(int(first_start), int(first_end)+1))
    second_num_range = set(range(int(second_start), int(second_end)+1))
    intersection_ = first_num_range.intersection(second_num_range)
    if len(longest_intersection) < len(intersection_):
        longest_intersection = intersection_

ordered_longest_intersection = sorted(longest_intersection)
print(f"Longest intersection is {ordered_longest_intersection} with length {len(longest_intersection)}")
