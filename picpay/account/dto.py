from dataclasses import dataclass


@dataclass
class AccountData:
    document_number: str
    first_name: str
    last_name: str
    email: str
    password: str
