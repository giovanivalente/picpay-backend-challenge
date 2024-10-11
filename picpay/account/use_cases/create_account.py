from rest_framework.exceptions import ValidationError

from picpay.account.dto import AccountData
from picpay.account.repositories import AccountRepository


class CreateAccount:
    def __init__(self, account_repository: AccountRepository):
        self._account_repository = account_repository

    def create_new_account(self, account_data: AccountData):
        self._validate_existing_account(account_data)

        new_account = self._account_repository.create_new_account_in_database(account_data)

        return new_account

    def _validate_existing_account(self, account_data: AccountData) -> None:
        account_already_exists = self._account_repository.check_unique_account_by_document_number_and_email(
            account_data
        )

        if account_already_exists:
            raise ValidationError('Account already exists with the given document number or email.')
