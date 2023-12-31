class dictionary_iter:
    def __init__(self, dict_: dict):
        self.dict_tuple = tuple(dict_.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dict_tuple):
            i = self.index
            self.index += 1
            return self.dict_tuple[i]
        else:
            raise StopIteration()

#test code:
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
