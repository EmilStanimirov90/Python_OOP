def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def double():

    x = 1

    while True:
        yield x
        x *= 2
        


generator = fibonacci()
generator2 = double()
for i in range(50):
    print(f"{next(generator)} {next(generator2)}")
