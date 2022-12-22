gifts = input().split()
 
index = int
current_gift = ''
gift_to_replace = ''
gift_to_remove = ''

current_action = input()

while current_action != "No Money":
    current_action = current_action.split()

    if current_action[0] == "OutOfStock"  :
 
        gift_to_remove = current_action[1]
 
        while gift_to_remove in gifts:
            index = gifts.index(gift_to_remove)
            gifts[index] = None

    elif current_action[0] == "Required":
 
        gift_to_replace = current_action[1]
        index = int(current_action[2])
        if len(gifts) > index >= 0:
            gifts[index] = gift_to_replace
 
    else:
 
        gifts[-1] = current_action[1]

    current_action = input()
 
print(' '.join(str(element) for element in gifts if element))
