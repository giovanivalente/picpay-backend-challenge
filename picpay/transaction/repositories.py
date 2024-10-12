from picpay.account.models import Account
from picpay.transaction.dto import DepositData
from picpay.transaction.enum import TransactionTypeEnum
from picpay.transaction.models import Transaction


class TransactionRepository:
    model = Transaction

    def create_new_deposit_in_database(self, deposit_data: DepositData, account: Account) -> Transaction:
        new_deposit = self.model(
            amount=deposit_data.amount,
            receiver=account,
            transaction_type=TransactionTypeEnum.DEPOSIT.value,
        )
        new_deposit.save()
        return new_deposit
