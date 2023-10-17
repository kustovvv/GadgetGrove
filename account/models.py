from django.db import models
from django.contrib.auth.models import User

class PersonalInformation(models.Model):
    user = models.ForeignKey(User, related_name='personal_information', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='personal_information_avatar', blank=True, null=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    married = models.CharField(max_length=255, null=True, blank=True)
    have_children = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    google = models.CharField(max_length=255, null=True, blank=True)
    pinterest = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    hobby = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

