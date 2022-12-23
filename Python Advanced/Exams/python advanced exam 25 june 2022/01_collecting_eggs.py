from collections import deque


egg_size = deque(input().split(", "))
paper_size = deque(input().split(", "))
box_size = 50
filled_boxes = 0


while egg_size and paper_size:
    egg = egg_size.popleft()
    paper = paper_size.pop()

    if int(egg) <= 0:
        paper_size.append(paper)
        continue

    if int(egg) == 13:
        paper_left = paper_size.popleft()
        paper_size.appendleft(paper)
        paper_size.append(paper_left)
        continue

    if box_size >= int(egg) + int(paper):
        filled_boxes += 1

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f"Eggs left: {', '.join(egg_size)}")

if paper_size:
    print(f"Pieces of paper left: {', '.join(paper_size)}")
