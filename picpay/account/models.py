from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django_extensions.db.models import TimeStampedModel
from rest_framework.exceptions import ValidationError

from picpay.account.enum import AccountTypeEnum
from picpay.settings import RAW_PF_DOCUMENT_LEN
from picpay.transaction.enum import TransactionTypeEnum


class Account(TimeStampedModel, AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    document_number = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    wallet = models.OneToOneField('wallet.Wallet', related_name='account_wallet', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'ACCOUNT'

    USERNAME_FIELD = 'document_number'
    EMAIL_FIELD = 'email'

    @property
    def get_account_type(self):
        account_type = (
            AccountTypeEnum.PF.value if len(self.document_number) == RAW_PF_DOCUMENT_LEN else AccountTypeEnum.PJ.value
        )

        return account_type

    def validate_transaction(self, transaction_type: str) -> None:
        if transaction_type == TransactionTypeEnum.DEPOSIT.value and self.get_account_type == AccountTypeEnum.PJ.value:
            raise ValidationError('Cannot deposit funds into a PJ account.')
