from rest_framework import serializers
from .models import JejuSchedule as jeju_schedule


class JejuScheduleSerializer(serializers.Serializer):
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
        model = jeju_schedule
        fileds = '__all__'

    def create(self, valideted_data):
        return jeju_schedule.objects.create(**valideted_data)

    def update(self, instance, valideted_data):
        jeju_schedule.objects.filter(pk=instance.username).update(**valideted_data)
