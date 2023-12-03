def get_primes(numbers: list):
    for number in numbers:
        if number < 2:
            continue
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number


print(list(get_primes([2, 4, 100_000_000_007, 5, 6, 9, 1, 0])))