from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from picpay.account.dto import AccountData
from picpay.account.factories import AccountFactory
from picpay.account.serializers import CreateAccountInputSerializer, CreateAccountOutputBaseSerializer


class CreateAccountAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_serializer = CreateAccountInputSerializer
        self.output_serializer = CreateAccountOutputBaseSerializer
        self.account_service = AccountFactory.make_create_account()

    def post(self, request: Request) -> Response:
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        account_data = AccountData(
            document_number=serializer.validated_data['document_number'],
            name=serializer.validated_data['name'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
        )

        new_account = self.account_service.create_new_account(account_data)

        output_serializer = self.output_serializer(instance=new_account)

        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)
