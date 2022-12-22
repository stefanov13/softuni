file_path = input().split(".")
file_name = file_path[0].split("\\")[-1]

print(f"File name: {file_name}")
print(f"File extension: {file_path[1]}")
