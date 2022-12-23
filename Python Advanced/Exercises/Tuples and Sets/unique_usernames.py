usernames_count = int(input())

unique_usernames = set()

for _ in range(usernames_count):
    unique_usernames.add(input())

print('\n'.join(unique_usernames))
