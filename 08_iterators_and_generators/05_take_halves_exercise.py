def solution():
    def integers():
        num = 0
        while True:
            num += 1
            yield num

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result

    return take, halves, integers


# test code:
int_ = solution()[2]
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

print(halves())
print(int_)
