from rest_framework import serializers

from picpay.utils.serializer import OutputBaseSerializer


class CreateAccountInputSerializer(serializers.Serializer):
    documentNumber = serializers.CharField(max_length=18, source='document_number')
    name = serializers.CharField(max_length=80)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)


class CreateAccountOutputBaseSerializer(OutputBaseSerializer):
    id = serializers.UUIDField()
    documentNumber = serializers.CharField(source='document_number')
    email = serializers.EmailField()
