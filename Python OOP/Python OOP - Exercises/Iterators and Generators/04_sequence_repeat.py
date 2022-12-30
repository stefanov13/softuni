class sequence_repeat:
    def __init__(self, sequence: str, num: int):
        self.sequence = list(sequence)
        self.num = num
        self.iter_count = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_count == self.num - 1:
            raise StopIteration

        self.iter_count += 1
        a = 5

        return self.sequence[self.iter_count % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
