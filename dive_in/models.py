from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=30)
    gold = models.IntegerField()
    silver = models.IntegerField()

    def __str__(self):
        return self.user.username
