from decimal import Decimal

from rest_framework import serializers

from picpay.utils.serializer import OutputBaseSerializer


class CreateDepositInputSerializer(serializers.Serializer):
    documentNumber = serializers.CharField(max_length=18, source='document_number')
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal(0.01))


class ReceiverOutputBaseSerializer(OutputBaseSerializer):
    name = serializers.CharField()
    documentNumber = serializers.CharField(source='document_number')


class CreateDepositOutputBaseSerializer(OutputBaseSerializer):
    transactionId = serializers.UUIDField(source='id')
    amount = serializers.DecimalField(decimal_places=2, max_digits=10)
    transactionType = serializers.CharField(source='transaction_type')
    receiver = ReceiverOutputBaseSerializer()
