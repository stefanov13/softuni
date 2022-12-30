class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.iter_count = self.count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_count == 0:
            raise StopIteration

        self.iter_count -= 1

        return self.iter_count


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
