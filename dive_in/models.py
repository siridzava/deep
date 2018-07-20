from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Character(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    character_name = models.CharField(max_length=30, unique=True)
    action_points = models.IntegerField()
    hit_points = models.IntegerField()
    crit_hit_points = models.IntegerField()
    gold = models.IntegerField()
    silver = models.IntegerField()

    def __str__(self):
        return self.user.username
