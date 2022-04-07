from django.db import models
from django.contrib.auth.models import *
# Create your models here.


class players(AbstractUser):
    email               = models.EmailField(max_length=25,               null=False, blank=False,    unique=True) 
    sports              = models.ManyToManyField('sports.sports',       related_name='sports')
    createdAt           = models.DateTimeField(auto_now_add=True) 

