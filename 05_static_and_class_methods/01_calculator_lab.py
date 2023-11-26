from functools import reduce


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for arg in args:
            result *= arg
        return result

    @staticmethod
    def divide(*args):
        result = 1
        for i in range(1, len(args)):
            if i == 1:
                result = args[0]
            if args[i] != 0:
                result /= args[i]
        return result


    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)



# test code :

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))