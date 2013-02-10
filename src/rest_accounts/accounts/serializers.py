from rest_framework import serializers
from accounts import models


class AccountSerializer(serializers.ModelSerializer):
    hotels = serializers.ManyPrimaryKeyRelatedField()

    class Meta:
        model = models.Account
        fields = (
            'username',
            'first_name',
            'last_name',
            'birth_date',
            'gender',
            'city',
            'country',
            'biography',
            'hotels',
        )


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotel
        fields = (
            'name',
            'city',
            'country',
            'description',
            'agent',
        )
