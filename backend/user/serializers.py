from rest_framework import serializers
from .models import User as user


class UserSerializer(serializers.Serializer):
    gender = serializers.CharField()
    mbti = serializers.CharField()

    class Meta:
        model = user
        fileds = '__all__'

    def create(self, valideted_data):
        return user.objects.create(**valideted_data)

    def update(self, instance, valideted_data):
        user.objects.filter(pk=instance.username).update(**valideted_data)
