from pycpfcnpj.mask import mask_cpf_cnpj
from rest_framework import serializers


class OutputBaseSerializer(serializers.Serializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if representation.get('documentNumber'):
            representation['documentNumber'] = mask_cpf_cnpj(representation['documentNumber'])

        return representation
