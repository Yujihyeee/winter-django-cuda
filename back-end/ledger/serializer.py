from rest_framework import serializers
from ledger.models import Ledger as ledger


class LedgerSerializer(serializers.Serializer):
    # date = serializers.DateField()
    category = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = ledger
        fileds = '__all__'

    def create(self, validated_data):
        return ledger.objects.create(**validated_data)

    def update(self, instance, validated_data):
        ledger.objects.filter(pk=instance.id).update(**validated_data)
