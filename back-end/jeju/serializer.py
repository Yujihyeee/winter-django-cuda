from rest_framework import serializers
from jeju.models import JejuSchedule as jeju


class JejuSerializer(serializers.Serializer):
    id = serializers.CharField()
    user = serializers.CharField()
    reg_date = serializers.DateTimeField()
    startday = serializers.DateField()
    endday = serializers.DateField()
    day = serializers.IntegerField()
    startloc = serializers.CharField()
    people = serializers.IntegerField()
    relationship = serializers.CharField()
    category = serializers.CharField()
    plane = serializers.CharField()
    acc = serializers.CharField()
    activity = serializers.CharField()
    olle = serializers.CharField()
    restaurant = serializers.CharField()
    tourism = serializers.CharField()
    shop = serializers.CharField()
    schedule = serializers.CharField()
    dday = serializers.DateField()

    class Meta:
        model = jeju
        fileds = '__all__'

    def create(self, validated_data):
        return jeju.objects.create(**validated_data)

    def update(self, instance, validated_data):
        jeju.objects.filter(pk=instance.id).update(**validated_data)
