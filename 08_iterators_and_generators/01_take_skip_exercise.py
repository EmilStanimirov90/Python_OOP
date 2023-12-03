class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.current_count:
            raise StopIteration()
        temp = self.current_count
        self.current_count += 1
        return temp * self.step


# test code:

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

# numbers = take_skip(10, 5)
# for number in numbers:
#     print(number)
