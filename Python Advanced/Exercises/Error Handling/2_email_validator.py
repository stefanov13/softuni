import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = (".com", ".bg", ".org", ".net")

name_pattern = r"[\w\.-]{5,}"
domain_pattern = r"[\.][a-z]{1,3}\b"

while True:
    email = input()

    if email == "End":
        break

    name_match = re.match(name_pattern, email.split("@")[0])
   
    if not name_match:
        raise NameTooShortError('Name must be more than 4 characters')

    elif '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')

    domain_match = re.findall(domain_pattern, email.split('@')[1])

    if domain_match:
        for domain in valid_domains:
            if domain == domain_match[0]:
                print("Email is valid")
                break
        else:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
