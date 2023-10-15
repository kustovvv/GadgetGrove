from django.db import models
from django.contrib.auth.models import User

class PersonalInformation(models.Model):
    user = models.ForeignKey(User, related_name='personal_information', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to='personal_information_avatar', blank=True, null=True)
    gender = models.CharField(max_length=255, null=True)
    married = models.CharField(max_length=255, null=True)
    have_children = models.CharField(max_length=255, null=True)
    birthday = models.IntegerField(null=True)
    birthmonth = models.CharField(max_length=10, null=True)
    birthyear = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=10, null=True)
    facebook = models.CharField(max_length=255, null=True)
    instagram = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    google = models.CharField(max_length=255, null=True)
    pinterest = models.CharField(max_length=255, null=True)
    about = models.TextField(null=True)
    hobby = models.TextField(null=True)
    interests = models.TextField(null=True)
