N = int(input())

for first in range(1, 10):
    if N % first == 0:
        for second in range(1, 10):
            if N % second == 0:
                for third in range(1, 10):
                    if N % third == 0:
                        for fourth in range(1, 10):
                            if N % fourth == 0:
                                print(f"{first}{second}{third}{fourth}", end=" ")
