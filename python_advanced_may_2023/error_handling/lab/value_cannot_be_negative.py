class ValueCannotBeNegative(Exception):
    """Raised when the input value is below zero"""
    pass


for i in range(5):
    num = int(input())
    if num < 0:
        raise ValueCannotBeNegative
