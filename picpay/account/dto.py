from dataclasses import dataclass


@dataclass(frozen=True)
class AccountData:
    document_number: str
    name: str
    email: str
    password: str
