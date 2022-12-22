def add_stop(index_to_add, element_to_add, current_tour_stops):
    index_to_add = int(index_to_add)
    if 0 <= index_to_add < len(current_tour_stops):
        firs_part = current_tour_stops[:index_to_add]
        second_part = current_tour_stops[index_to_add:]
        current_tour_stops = firs_part + element_to_add + second_part
    print_current_string(current_tour_stops)
    return current_tour_stops


def remove_stop(start_index, end_index, current_tour_stops):
    start_index = int(start_index)
    end_index = int(end_index)
    if 0 <= start_index < len(current_tour_stops) and 0 <= end_index < len(current_tour_stops):
        part_for_remove = current_tour_stops[start_index:end_index+1]
        current_tour_stops = current_tour_stops.replace(part_for_remove, "")
    print_current_string(current_tour_stops)
    return current_tour_stops


def switch(old_string, new_string, current_tour_stops):
    if old_string in current_tour_stops:  # while old_string in current_tour_stops:
        current_tour_stops = current_tour_stops.replace(old_string, new_string)
    print_current_string(current_tour_stops)
    return current_tour_stops


def print_current_string(current_tour_stops):
    print(current_tour_stops)



tour_stops = input()
manipulation_command = input()

while not manipulation_command == "Travel":
    manipulation_command = manipulation_command.split(":")
    manipulation_action = manipulation_command[0]
    first_parameter = manipulation_command[1]
    second_paraneter = manipulation_command[2]
    if manipulation_action == "Add Stop":
        tour_stops = add_stop(first_parameter, second_paraneter, tour_stops)
    elif manipulation_action == "Remove Stop":
        tour_stops = remove_stop(first_parameter, second_paraneter, tour_stops)
    elif manipulation_action == "Switch":
        tour_stops = switch(first_parameter, second_paraneter, tour_stops)
    manipulation_command = input()

print(f"Ready for world tour! Planned stops: {tour_stops}")
