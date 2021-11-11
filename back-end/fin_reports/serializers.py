from rest_framework import serializers
from .models import FinReports as finReports


class FinReportsSerializer(serializers.Serializer):
    factory = serializers.CharField()
    category = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = finReports
        fileds = '__all__'

    def create(self, valideted_data):
        return finReports.objects.create(**valideted_data)

    def update(self, instance, valideted_data):
        finReports.objects.filter(pk=instance.username).update(**valideted_data)
