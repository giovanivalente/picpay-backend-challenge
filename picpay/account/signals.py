from django.db.models.signals import post_save
from django.dispatch import receiver

from picpay.account.models import Account
from picpay.wallet.models import Wallet


@receiver(post_save, sender=Account)
def create_wallet_for_account(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.create(account=instance)

        instance.wallet = wallet
        instance.save(update_fields=['wallet'])
