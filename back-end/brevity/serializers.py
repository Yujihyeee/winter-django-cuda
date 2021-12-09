from rest_framework import serializers
from .models import Brevity as brevity


class FinReportsSerializer(serializers.Serializer):
    userid = serializers.IntegerField()
    plane = serializers.CharField()
    accommodation = serializers.CharField()
    activity = serializers.CharField(null=True)
    restaurant = serializers.CharField(null=True)
    shop = serializers.CharField(null=True)
    tourism = serializers.CharField(null=True)
    olle = serializers.CharField(null=True)
    option = serializers.CharField()

    class Meta:
        model = brevity
        fileds = '__all__'

    def create(self, valideted_data):
        return brevity.objects.create(**valideted_data)

    def update(self, instance, valideted_data):
        brevity.objects.filter(pk=instance.username).update(**valideted_data)
