from django.urls import path

from picpay.account.views.create_account_api_view import CreateAccountAPIView

app_name = 'account'

urlpatterns = [
    path('account/create', CreateAccountAPIView.as_view(), name='create-account'),
]
