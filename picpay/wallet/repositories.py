from decimal import Decimal

from picpay.account.models import Account
from picpay.wallet.models import Wallet


class WalletRepository:
    model = Wallet

    def update_wallet_balance(self, amount: Decimal, account: Account) -> Wallet:
        wallet = self.model.objects.get(account=account)
        wallet.balance += amount
        wallet.save()
        return wallet
