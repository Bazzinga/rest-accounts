from rest_framework import serializers
from accounts import models


class AccountSerializer(serializers.ModelSerializer):
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
        )


class HotelSerializer(serializers.ModelSerializer):
    agent = serializers.Field(source='agent.username')

    class Meta:
        model = models.Hotel
        fields = (
            'name',
            'city',
            'country',
            'description',
            'agent',
        )
