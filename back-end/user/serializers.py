from rest_framework import serializers
from .models import User as user


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    # username = serializers.CharField()
    # password = serializers.CharField()
    # name = serializers.CharField()
    # email = serializers.EmailField()
    # birth = serializers.DateField()
    gender = serializers.CharField()
    mbti = serializers.CharField()
    # mbti_list = serializers.CharField()
    # card_number = serializers.IntegerField()
    # card_company = serializers.CharField()
    # regDate = serializers.DateField()

    class Meta:
        model = user
        fields = '__all__'

    def create(self, validated_data):
        return user.objects.create(**validated_data)

    def update(self, instance, validated_data):
        user.objects.filter(pk=instance.id).update(**validated_data)
