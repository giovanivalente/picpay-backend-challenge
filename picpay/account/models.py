from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import UniqueConstraint
from django_extensions.db.models import TimeStampedModel

from picpay.account.entities import AccountEntity


class Account(TimeStampedModel, AbstractBaseUser, AccountEntity):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    document_number = models.CharField(max_length=14, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'ACCOUNT'
        constraints = [UniqueConstraint(fields=['document_number', 'email'], name='unique_account')]

    USERNAME_FIELD = 'document_number'
    EMAIL_FIELD = 'email'
