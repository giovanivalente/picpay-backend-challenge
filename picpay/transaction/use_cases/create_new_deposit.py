from picpay.account.use_cases.db_get_account import DbGetAccount
from picpay.transaction.dto import DepositData
from picpay.transaction.enum import TransactionTypeEnum
from picpay.transaction.models import Transaction
from picpay.transaction.repositories import TransactionRepository
from picpay.wallet.repositories import WalletRepository


class CreateNewDeposit:
    def __init__(
        self,
        db_get_account: DbGetAccount,
        transaction_repository: TransactionRepository,
        wallet_repository: WalletRepository,
    ):
        self._db_get_account = db_get_account
        self._transaction_repository = transaction_repository
        self._wallet_repository = wallet_repository

    def create_deposit(self, deposit_data: DepositData) -> Transaction:
        account = self._db_get_account.get_account_by_document_number(document_number=deposit_data.document_number)
        account.validate_transaction(transaction_type=TransactionTypeEnum.DEPOSIT.value)

        deposit = self._transaction_repository.create_new_deposit_in_database(deposit_data, account)

        self._wallet_repository.update_wallet_balance(amount=deposit_data.amount, account=account)

        return deposit
