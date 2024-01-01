from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)])
    is_email_verified = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
