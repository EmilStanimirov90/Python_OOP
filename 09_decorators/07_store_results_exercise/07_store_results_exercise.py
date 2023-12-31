def store_results(func):
    def wrapper(a, b):
        with open('results.txt', 'a') as file:
            file.write(f"Function '{func.__name__}' was called. Result: {func(a, b)}\n")

    return wrapper


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
