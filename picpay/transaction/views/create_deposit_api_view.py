from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from picpay.transaction.dto import DepositData
from picpay.transaction.factories import TransactionFactory
from picpay.transaction.serializers import CreateDepositInputSerializer, CreateDepositOutputBaseSerializer


class CreateDepositAPIView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transaction_service = TransactionFactory.make_create_new_deposit()
        self.input_serializer = CreateDepositInputSerializer
        self.output_serializer = CreateDepositOutputBaseSerializer

    def post(self, request: Request) -> Response:
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        deposit_data = DepositData(
            document_number=serializer.validated_data.get('document_number'),
            amount=serializer.validated_data.get('amount'),
        )

        deposit = self.transaction_service.create_deposit(deposit_data)

        output_serializer = self.output_serializer(instance=deposit)

        return Response(data=output_serializer.data, status=status.HTTP_200_OK)
