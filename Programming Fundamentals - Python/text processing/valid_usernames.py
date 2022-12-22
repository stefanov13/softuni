special_characters = " !@#$%^&*()+?=,<>/`~|'\""
usernames = input().split(", ")
valid_usernames = []

for username in usernames:
    if any(_ in special_characters for _ in username):
        continue
    if 3 <= len(username) <= 16:
        valid_usernames.append(username)

for valid_username in valid_usernames:
    print(valid_username)
