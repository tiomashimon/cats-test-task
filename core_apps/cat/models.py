from django.db import models

from ..user.models import User


class Cat(models.Model):
    cat_id = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, default=1, related_name="cats", on_delete=models.CASCADE
    )
    width = models.IntegerField(default=480)
    height = models.IntegerField(default=480)

    def __str__(self):
        return self.cat_id


class CatVote(models.Model):
    user = models.ForeignKey(User, related_name='votes_given', on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, related_name='votes_received', on_delete=models.CASCADE)
    vote = models.IntegerField()
