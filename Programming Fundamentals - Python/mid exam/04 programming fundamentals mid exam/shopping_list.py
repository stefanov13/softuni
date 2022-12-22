def urgent(item):
    if item not in shoping_list:
        shoping_list.insert(0, item)
    return shoping_list


def unnecessary(item):
    if item in shoping_list:
        shoping_list.remove(item)
    return shoping_list


def corect(old_item, new_item):
    if old_item in shoping_list:
        index_old_item = shoping_list.index(old_item)
        shoping_list.remove(old_item)
        shoping_list.insert(index_old_item, new_item)
    return shoping_list    


def rearrange(item):
    if item in shoping_list:
        shoping_list.remove(item)
        shoping_list.append(item)
    return shoping_list


shoping_list = input().split("!")
new_entry = input().split()

while new_entry[0] not in "Go Shopping!":
    if new_entry[0] in "Urgent":
        urgent(new_entry[1])
    elif new_entry[0] in "Unnecessary":
        unnecessary(new_entry[1])
    elif new_entry[0] in "Correct":
        corect(new_entry[1], new_entry[2])
    elif new_entry[0] in "Rearrange":
        rearrange(new_entry[1])
    new_entry = input().split()

print(", ".join(shoping_list))
