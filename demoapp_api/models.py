from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# -------------------------------------------- Model ------------------------------------------ #

class UserModel(AbstractUser):
    fullname = models.CharField(max_length=2000) 
    createdAt = models.DateTimeField(auto_now_add=True) 
    
class TableOfContentModel(models.Model):
    description = models.CharField(max_length=2000, null=False, blank=False)
    sub_section = models.ForeignKey("self", on_delete=models.SET_NULL, related_name='tableofcontent_sub_section', null=True, blank=True) 
    
