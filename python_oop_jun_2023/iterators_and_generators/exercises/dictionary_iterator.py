class dictionary_iter:
    def __init__(self, my_dict: dict):
        self.dict_items = list(my_dict.items())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.dict_items) - 1:
            raise StopIteration

        self.idx += 1

        return self.dict_items[self.idx]


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

