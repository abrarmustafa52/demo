from .models import * 
from rest_framework import serializers
 

# -------------------------------------------- REGISTRATION MODELS------------------------------------------ #
class TableOfContentSer(serializers.ModelSerializer):
    class Meta:
        model = TableOfContentModel
        fields = '__all__'
      
 