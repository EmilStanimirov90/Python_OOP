def reverse_text(string):
    start_index = 0
    end_index = len(string) - 1
    while start_index <= end_index:
        yield string[end_index]
        end_index -= 1



for char in reverse_text("step"):
    print(char, end='')
