class dictionary_iter:
    def __init__(self, iter_dict: dict):
        self.iter_dict = list(iter_dict.items())
        self.iter_count = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_count == len(self.iter_dict) -1:
            raise StopIteration

        self.iter_count += 1
        output = self.iter_dict[self.iter_count]
        
        return output[0], output[1]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
