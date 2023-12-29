from django.db import models
from authentication.models import User as CustomUser


class PersonalInformation(models.Model):
    user = models.ForeignKey(CustomUser, related_name='personal_information_user', on_delete=models.CASCADE)
    avatar_url = models.ImageField(upload_to='personal_information_avatar', blank=True, null=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    married = models.BooleanField(default=False)
    have_children = models.BooleanField(default=False, null=True)
    birthday = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    google_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    hobby = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
