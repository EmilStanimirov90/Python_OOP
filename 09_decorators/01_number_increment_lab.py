def number_increment(numbers):
    def increase():
        new_numbers = []
        for el in numbers:
            new_numbers.append(el + 1)
        return new_numbers

    return increase()


print(number_increment([1, 2, 3]))
