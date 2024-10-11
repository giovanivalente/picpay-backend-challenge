from datetime import datetime
from uuid import UUID


class AccountEntity:
    created: datetime
    modified: datetime
    last_login: datetime
    id: UUID
    name: str
    document_number: str
    email: str
    password: str
