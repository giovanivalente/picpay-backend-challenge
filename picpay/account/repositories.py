from dataclasses import asdict

from django.db.models import Q

from picpay.account.dto import AccountData
from picpay.account.entities import AccountEntity
from picpay.account.models import Account


class AccountRepository:
    model = Account

    def create_new_account_in_database(self, account_data: AccountData) -> AccountEntity:
        new_account = self.model(**asdict(account_data))
        new_account.set_password(account_data.password)
        new_account.save()
        return new_account

    def check_unique_account_by_document_number_and_email(self, account_data: AccountData) -> bool:
        account_exist = self.model.objects.filter(
            Q(document_number=account_data.document_number) | Q(email=account_data.email)
        ).exists()

        return account_exist
