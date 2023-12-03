def possible_permutations(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for i in range(len(lst)):
            current_element = lst[i]
            remaining_elements = lst[:i] + lst[i+1:]
            for perm in possible_permutations(remaining_elements):
                yield [current_element] + perm








[print(n) for n in possible_permutations([1, 2, 3])]