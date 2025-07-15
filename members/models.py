from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, unique=True)
    age = models.IntegerField()
    matches_played = models.IntegerField()


class PlayerManager(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=50, blank=False)
