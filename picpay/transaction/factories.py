from picpay.account.factories import AccountFactory
from picpay.transaction.repositories import TransactionRepository
from picpay.transaction.use_cases.create_new_deposit import CreateNewDeposit
from picpay.wallet.factories import WalletFactory


class TransactionFactory:
    @classmethod
    def make_transaction_repository(cls) -> TransactionRepository:
        return TransactionRepository()

    @classmethod
    def make_create_new_deposit(cls) -> CreateNewDeposit:
        return CreateNewDeposit(
            db_get_account=AccountFactory.make_db_get_account(),
            transaction_repository=cls.make_transaction_repository(),
            wallet_repository=WalletFactory.make_wallet_repository(),
        )
