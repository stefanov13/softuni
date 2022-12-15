searched_book = input()
library_capacity = int(input())

counter = 0
book_is_find = False
while counter < library_capacity:
    library_book = input()
    if library_book == searched_book:
        book_is_find = True
        break
    counter += 1

if book_is_find:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {library_capacity} books.")
