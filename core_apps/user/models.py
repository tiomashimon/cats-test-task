from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email_verificated = models.BooleanField(default=False)