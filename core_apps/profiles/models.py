from django.db import models

from ..user.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField()

    def __str__(self):
        return self.user.username
