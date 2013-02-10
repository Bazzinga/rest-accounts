from django.db import models
from django.contrib.auth.models import User


class Account(User):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    birth_date = models.DateTimeField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ('username',)

    def __unicode__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
