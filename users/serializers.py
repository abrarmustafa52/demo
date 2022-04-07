from .models import * 
from rest_framework import serializers
from sports.serializers import *
 

# -------------------------------------------- REGISTRATION MODELS------------------------------------------ #
class UserSer(serializers.ModelSerializer):
    sports = SportsSer(read_only=True, many=True)
    class Meta:
        model = players
        fields = '__all__'
      
 