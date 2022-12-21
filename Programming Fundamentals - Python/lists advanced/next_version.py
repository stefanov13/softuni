version = input().split(".")
res = "".join(version)
# for x in version:
#     res += str(x)

int_res = int(res) + 1

str_res = str(int_res)

print(f"{str_res[0]}.{str_res[1]}.{str_res[2]}")
