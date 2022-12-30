def fibonacci():
    first_num, second_num = 0, 1

    while True:
        yield first_num
        
        first_num, second_num = second_num, first_num + second_num

    
generator = fibonacci()
for i in range(5):
    print(next(generator))
