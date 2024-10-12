from picpay.wallet.repositories import WalletRepository


class WalletFactory:
    @classmethod
    def make_wallet_repository(cls) -> WalletRepository:
        return WalletRepository()
