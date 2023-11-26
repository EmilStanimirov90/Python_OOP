class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, roman):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0

        for letter in roman:
            curr_value = roman_dict[letter]
            if curr_value > prev_value:
                # If the current value is greater than the previous, it means subtraction
                result += curr_value - 2 * prev_value
            else:
                result += curr_value
            prev_value = curr_value

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"


#test code :

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))