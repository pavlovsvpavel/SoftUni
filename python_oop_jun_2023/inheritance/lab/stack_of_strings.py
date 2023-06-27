from typing import List


class Stack:
    def __init__(self):
        self.data: List = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> None:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self):
        return "[" + ', '.join(reversed(self.data)) + "]"


some_string = Stack()
some_string.push("test")
some_string.push("test2")
some_string.push("test3")
some_string.pop()

print(some_string.top())
print(some_string.is_empty())
print(some_string)
