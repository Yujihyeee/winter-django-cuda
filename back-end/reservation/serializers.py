from rest_framework import serializers
from .models import Reservation as reservation


class ReservationSerializer(serializers.Serializer):
    schedule = serializers.CharField()
    voucher = serializers.CharField()
    caution = serializers.CharField()
    fees = serializers.IntegerField()
    client = serializers.CharField()

    class Meta:
        model = reservation
        fileds = '__all__'

    def create(self, valideted_data):
        return reservation.objects.create(**valideted_data)

    def update(self, instance, valideted_data):
        reservation.objects.filter(pk=instance.username).update(**valideted_data)
