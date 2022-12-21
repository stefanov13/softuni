def merge(start_index, end_index, array):
    if start_index < 0:
        start_index = 0
    cuted_part = array[start_index:end_index + 1]
    concat_element = ""
    if cuted_part:
        concat_element = "".join(cuted_part)
    else:
        return array
    array[start_index] = concat_element
    del array[start_index+1:end_index+1]
    return array


def divide(el, parts_count, array):
    if parts_count in (0, 1):
        return array
    element_for_divide = array[el]
    remainder = len(element_for_divide) % parts_count
    elements_length = len(element_for_divide) // parts_count
    divided_elements = [element_for_divide[i:i+elements_length] for i in range(0, len(element_for_divide) - remainder, elements_length)]
    if remainder == 0:
        add_divided_elements(el, divided_elements, array)
        return array
    else:
        divided_elements[-1] += element_for_divide[-remainder:]
        add_divided_elements(el, divided_elements, array)
        return array
    

def add_divided_elements(el, divided_elements, array):
    array.pop(el)
    for divided_element in divided_elements[::-1]:
        array.insert(el, divided_element)
    return array


given_sequence = input().split()

commands = input()

while commands != "3:1":
    action, first_segment, second_segment = commands.split()
    if action == "merge":
        given_sequence = merge(int(first_segment), int(second_segment), given_sequence)
    elif action == "divide":
        given_sequence = divide(int(first_segment), int(second_segment), given_sequence)
    commands = input()

print(" ".join(given_sequence))
