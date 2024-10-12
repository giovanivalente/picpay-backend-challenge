from typing import Optional

from rest_framework.exceptions import NotFound

from picpay.account.models import Account
from picpay.account.repositories import AccountRepository


class DbGetAccount:
    def __init__(self, account_repository: AccountRepository):
        self._account_repository = account_repository

    def get_account_by_document_number(self, document_number: str, raise_exception: bool = True) -> Optional[Account]:
        account = self._account_repository.get_account_by_document_number(document_number)

        if not account and raise_exception:
            raise NotFound(detail='Account not found.')

        return account
