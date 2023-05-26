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

while True:
    email = input()

    if email == "End":
        break

    symbol_counter = email.count("@")
    name_validator = bool(re.search(name_pattern, email))
    domain_validator = bool(re.search(domain_pattern, email))

    if not name_validator:
        raise NameTooShortError("Name must be more than 4 characters")

    elif symbol_counter > 1:
        raise MustContainOnlyOneAtSymbolError("Email must contain only one '@' symbol")

    elif not symbol_counter:
        raise MustContainAtSymbolError("Email must contain @")

    elif not domain_validator:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print("Email is valid")
