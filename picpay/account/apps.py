from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'picpay.account'

    @classmethod
    def ready(cls):
        import picpay.account.signals  # noqa F401
