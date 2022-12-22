food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
pet_weight = float(input()) * 1000


for day in range(1, 30 + 1):
    food -= 300
    if day % 2 == 0:
        hay -= food / 20
    if day % 3 == 0:
        cover -= pet_weight / 3
    
if food <= 0 or hay <= 0 or cover <= 0:
    print(f"Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
