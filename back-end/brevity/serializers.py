from rest_framework import serializers
from .models import Brevity as brevity


class FinReportsSerializer(serializers.Serializer):
    userid = serializers.IntegerField()
    plane = serializers.IntegerField()
    accommodation = serializers.IntegerField()
    activity = serializers.IntegerField()
    option = serializers.IntegerField()

    class Meta:
        model = brevity
        fileds = '__all__'

    def create(self, valideted_data):
        return brevity.objects.create(**valideted_data)

    def update(self, instance, valideted_data):
        brevity.objects.filter(pk=instance.username).update(**valideted_data)
