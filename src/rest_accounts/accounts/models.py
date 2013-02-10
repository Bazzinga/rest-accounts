from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
)


class Account(User):
    birth_date = models.DateTimeField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    city = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    biography = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('username',)

    def __unicode__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    agent = models.ForeignKey(User)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name
