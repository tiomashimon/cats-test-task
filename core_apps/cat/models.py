from django.db import models
from ..user.models import User

class Cat(models.Model):
    cat_id = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    user = models.ForeignKey(User, default=1, related_name='cats', on_delete=models.CASCADE)

    def __str__(self):
        return self.cat_id