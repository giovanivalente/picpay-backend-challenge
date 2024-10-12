from uuid import uuid4

from django.db import models
from django_extensions.db.models import TimeStampedModel

from picpay.account.models import Account


class Transaction(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    sender = models.ForeignKey(Account, related_name='sender_transactions', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(Account, related_name='receiver_transactions', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=8)

    class Meta:
        db_table = 'TRANSACTION'
