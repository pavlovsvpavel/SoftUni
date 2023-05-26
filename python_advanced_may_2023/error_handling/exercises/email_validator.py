import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlyOneAtSymbolError(Exception):
    pass


name_pattern = r"\w{5,}"
domain_pattern = r"\.com$|\.bg$|\.net$|\.org$"

email = input()

while email != "End":
    symbol_idx = [email.index(el) for el in email if el == "@"]
    name_validator = bool(re.search(name_pattern, email))
    domain_validator = bool(re.search(domain_pattern, email))

    if not name_validator:
        raise NameTooShortError("Name must be more than 4 characters")

    elif len(symbol_idx) > 1:
        raise MustContainOnlyOneAtSymbolError("Email must contain only one '@' symbol")

    elif not symbol_idx:
        raise MustContainAtSymbolError("Email must contain @")

    elif not domain_validator:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print("Email is valid")

    email = input()
