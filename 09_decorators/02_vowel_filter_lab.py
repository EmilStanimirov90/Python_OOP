def vowel_filter(function):

    def wrapper():
        list_ = function()
        vowels = "aeuiyo" #AEUIOY"
        result = []
        for el in list_:
            if el.lower() in vowels:
                result.append(el)

        return result
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e", "A"]

print(get_letters())
