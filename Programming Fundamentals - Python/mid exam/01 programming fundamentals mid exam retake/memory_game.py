def check_indexes(strike1, strike2):
    adding = "-" + str(trying) + "a"
    if strike1 == strike2:
        for _ in range(2):
            sequence_str.insert(len(sequence_str) // 2, adding)
        return True
    elif strike[0] not in range(len(sequence_str)) or strike[1] not in range(len(sequence_str)):
        for _ in range(2):
            sequence_str.insert(len(sequence_str) // 2, adding)
        return True


sequence_str = input().split()

strike = input()
trying = 1

while strike not in "end":
    if sequence_str == []:
        strike = input()
        continue
    strike = list(map(int, strike.split()))
    if check_indexes(strike[0], strike[1]):
        print("Invalid input! Adding additional elements to the board")
    elif sequence_str[strike[0]] == sequence_str[strike[1]]:
        removed_element = sequence_str[strike[0]]
        print(f"Congrats! You have found matching elements - {removed_element}!")
        for _ in range(2):
            sequence_str.remove(removed_element)
    else:
        print("Try again!")
    if sequence_str == []:
        print(f"You have won in {trying} turns!")
    trying += 1
    strike = input()

if sequence_str:
    result = " ".join(sequence_str)
    print("Sorry you lose :(")
    print(result)
