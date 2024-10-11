from decimal import Decimal
from uuid import uuid4

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Wallet(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal(0))
    account = models.OneToOneField('account.Account', related_name='account_wallet', on_delete=models.CASCADE)

    class Meta:
        db_table = 'WALLET'
