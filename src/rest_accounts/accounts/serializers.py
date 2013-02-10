from django.forms import widgets
from rest_framework import serializers
from accounts import models


class AccountSerializer(serializers.Serializer):
    pk = serializers.Field()
    username = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    birth_date = serializers.DateTimeField()
    gender = serializers.ChoiceField(choices=models.GENDER_CHOICES)
    city = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
    biography = serializers.CharField(widget=widgets.Textarea)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new account.
        """
        if instance:
            # Update existing instance.
            instance.username = attrs.get('username', instance.username)
            instance.first_name = attrs.get('first_name', instance.first_name)
            instance.last_name = attrs.get('last_name', instance.last_name)
            instance.email = attrs.get('email', instance.email)
            instance.birth_date = attrs.get('birth_date', instance.birth_date)
            instance.gender = attrs.get('gender', instance.gender)
            instance.city = attrs.get('city', instance.city)
            instance.country = attrs.get('country', instance.country)
            instance.biography = attrs.get('biography', instance.biography)

            return instance

        # Create new instance.
        return models.Account(**attrs)
