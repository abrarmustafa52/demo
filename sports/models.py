from django.db import models

# Create your models here.

# -------------------------------------------- Model ------------------------------------------ #

class sports(models.Model):
    name            = models.CharField(max_length=2000, null=False, blank=False, choices=sports_choices)
    players         = models.ManyToManyField('users.players', related_name='players')
    
 