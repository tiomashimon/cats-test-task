from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email_verificated = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Verification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    code = models.IntegerField()
    is_alive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email