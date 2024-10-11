from rest_framework import serializers


class CreateAccountInputSerializer(serializers.Serializer):
    documentNumber = serializers.CharField(max_length=18, source='document_number')
    firstName = serializers.CharField(max_length=25, source='first_name')
    lastName = serializers.CharField(max_length=25, source='last_name')
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)


class CreateAccountOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    documentNumber = serializers.CharField(read_only=True, source='document_number')
    email = serializers.EmailField(read_only=True)
