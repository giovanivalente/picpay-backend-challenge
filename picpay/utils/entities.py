from datetime import datetime
from decimal import Decimal
from uuid import UUID


class BaseEntity:
    created: datetime
    modified: datetime


class AccountEntity(BaseEntity):
    last_login: datetime
    id: UUID
    name: str
    document_number: str
    email: str
    password: str
    wallet: 'WalletEntity'


class WalletEntity(BaseEntity):
    id: UUID
    balance: Decimal
    account: 'AccountEntity'
