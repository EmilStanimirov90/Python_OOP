def print_row(n,row):
    print(" " * (n - row), end='')
    print(*["*"] * row)


def print_triangle(n):
    for row in range(1, n + 1):
        print_row(n, row)


def print_reverse(n):
    for r in range(n - 1, 0, -1):
        print_row(n, r)


def create_rhombus(n):
    print_triangle(n)
    print_reverse(n)


n = int(input())
create_rhombus(n)




