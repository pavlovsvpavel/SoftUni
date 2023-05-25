import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

while email != "End":
    symbol_idx = [email.index(el) for el in email if el == "@"]

    if not symbol_idx:
        raise MustContainAtSymbolError("MustContainAtSymbolError")

    name = email[:symbol_idx[0]]
    pattern = r"\.com$|\.bg$|\.net$|\.org$"
    domain_validator = bool(re.search(pattern, email))

    if len(name) < 5:
        raise NameTooShortError("NameTooShortError")

    elif not domain_validator:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print("Email is valid")

    email = input()
