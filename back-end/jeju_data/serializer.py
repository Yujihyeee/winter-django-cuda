from rest_framework import serializers
# pip install Django django-rest-framework
from .models import Tourism as tourism
from .models import Activity as activity
from .models import Plane as plane
from .models import Shop as shop
from .models import Restaurant as restaurant
from .models import Accommodation as accommodation
from .models import Olle as olle

class TourismSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    address = serializers.CharField()
    explanation = serializers.CharField()
    tour_category_id = serializers.CharField()
    image_id = serializers.CharField()
    lat = serializers.CharField()
    log = serializers.CharField()

    class Meta:
        model = tourism
        fields = '__all__'

class ActivitySerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    start_business_time = serializers.CharField()
    end_business_time = serializers.CharField()
    time = serializers.CharField()
    contact = serializers.CharField()
    loc = serializers.CharField()
    price = serializers.CharField()
    act_category_id = serializers.CharField()
    lat = serializers.CharField()
    log = serializers.CharField()
    image_id = serializers.CharField()

    class Meta:
        model = activity
        fields = '__all__'

class PlaneSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    plane_category_id = serializers.CharField()
    vihicleId = serializers.CharField()
    airlineNm = serializers.CharField()
    depPlandTime = serializers.CharField()
    arrPlandTime = serializers.CharField()
    economyCharge = serializers.CharField()

    class Meta:
        model = plane
        fields = '__all__'

class ShopSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    loc = serializers.CharField()
    explanation = serializers.CharField()
    category_id = serializers.CharField()
    recommend = serializers.CharField()
    image_id = serializers.CharField()
    lat = serializers.CharField()
    log = serializers.CharField()

    class Meta:
        model = shop
        fields = '__all__'


class RestaurantSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    res_category_id = serializers.CharField()
    loc = serializers.CharField()
    recommend = serializers.CharField()
    image_id = serializers.CharField()
    lat = serializers.CharField()
    log = serializers.CharField()

    class Meta:
        model = restaurant
        fields = '__all__'


class AccommodationSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    loc = serializers.CharField()
    acc_category_id = serializers.CharField()
    price = serializers.CharField()
    contact = serializers.CharField()
    standard_number = serializers.CharField()
    image_id = serializers.CharField()
    lat = serializers.CharField()
    log = serializers.CharField()

    class Meta:
        model = accommodation
        fields = '__all__'

class OlleSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    category_id = serializers.CharField()
    course = serializers.CharField()
    name = serializers.CharField()
    distance = serializers.CharField()
    time = serializers.CharField()
    starting_point = serializers.CharField()
    end_point = serializers.CharField()
    explanation = serializers.CharField()
    image_id = serializers.CharField()
    lat = serializers.CharField()
    log = serializers.CharField()

    class Meta:
        model = olle
        fields = '__all__'