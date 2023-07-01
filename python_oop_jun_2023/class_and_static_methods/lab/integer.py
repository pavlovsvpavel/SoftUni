from math import floor


class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"

        float_value = floor(float_value)

        return cls(float_value)

    @classmethod
    def from_roman(cls, roman_num):
        roman_num = roman_num.upper()
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0

        for i in range(len(roman_num) - 1):
            if roman[roman_num[i]] < roman[roman_num[i + 1]]:
                num += roman[roman_num[i]] * -1
                continue

            num += roman[roman_num[i]]

        num += roman[roman_num[-1]]

        return cls(num)

    @classmethod
    def from_string(cls, value):
        if not str(value).isdigit():
            return "wrong type"

        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

