from django.db import models

class User(models.Model):
    user_id = models.IntegerField(default=0, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    lang = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    step = models.IntegerField(default=0)
    izoh = models.TextField(max_length=200, blank=True, null=True)