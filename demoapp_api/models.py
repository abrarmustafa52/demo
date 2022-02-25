from django.db import models
 

# Create your models here.

# -------------------------------------------- Model ------------------------------------------ #

class TableOfContentModel(models.Model):
    description = models.CharField(max_length=2000, null=False, blank=False)
    parent_section = models.ForeignKey("self", on_delete=models.SET_NULL, related_name='tableofcontent_parent_section', null=True, blank=True) 
    
