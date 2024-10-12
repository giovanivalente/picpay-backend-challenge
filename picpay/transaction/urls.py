from django.urls import path

from picpay.transaction.views.create_deposit_api_view import CreateDepositAPIView

app_name = 'transaction'

urlpatterns = [
    path('transaction/deposit', CreateDepositAPIView.as_view(), name='deposit'),
]
