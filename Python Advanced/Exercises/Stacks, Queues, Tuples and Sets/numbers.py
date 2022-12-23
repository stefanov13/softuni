def add(nums_to_add, sequence):
    a = [sequence.add(int(digit)) for digit in nums_to_add]
    return sequence


def remove(nums_for_removing, sequence):
    for el in nums_for_removing:
        sequence.discard(int(el))
    return sequence


def check_subset(sequence_one, sequence_two):
    if sequence_one.issubset(sequence_two):
        print("True")
    elif sequence_two.issubset(sequence_one):
        print("True")
    else:
        print("False")


first_sequence = set(int(num) for num in input().split())
second_sequence = set(int(num) for num in input().split())

commands_count = int(input())

for i in range(commands_count):
    action_command = input().split()
    if action_command[0] == "Add":
        if action_command[1] == "First":
            first_sequence = add(action_command[2:], first_sequence)
        else:
            second_sequence = add(action_command[2:], second_sequence)
    elif action_command[0] == "Remove":
        if action_command[1] == "First":
            first_sequence = remove(action_command[2:], first_sequence)
        else:
            second_sequence = remove(action_command[2:], second_sequence)
    else:
        check_subset(first_sequence, second_sequence)

print(*sorted(set(first_sequence)), sep=", ")
print(*sorted(set(second_sequence)), sep=", ")
