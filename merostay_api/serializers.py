from rest_framework import serializers
from .models import hotel_info

class Hotel_info_serializer(serializers.ModelSerializer):
    class Meta:
        model=hotel_info
        fields="__all__"