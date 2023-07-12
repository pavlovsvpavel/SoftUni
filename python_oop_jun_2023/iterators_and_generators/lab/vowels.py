class vowels:
    VOWELS = "aeiouy"

    def __init__(self, text: str) -> None:
        self.text = text
        self.start = 0
        self.end = len(self.text) - 1

    def __iter__(self) -> object:
        return self

    def __next__(self) -> str:
        while self.start <= self.end:
            letter = self.text[self.start]
            self.start += 1

            if letter.lower() in vowels.VOWELS:
                return letter

        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

