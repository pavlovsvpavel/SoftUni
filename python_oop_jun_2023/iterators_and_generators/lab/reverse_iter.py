class reverse_iter:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.start = len(self.iterable) - 1

    def __iter__(self) -> object:
        return self

    def __next__(self) -> int:
        if self.start < 0:
            raise StopIteration()

        number = self.iterable[self.start]
        self.start -= 1

        return number


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
