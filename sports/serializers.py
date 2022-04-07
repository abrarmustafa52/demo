from users.models import players
from .models import * 
from rest_framework import serializers
 

# -------------------------------------------- REGISTRATION MODELS------------------------------------------ #
class PlayerSer(serializers.ModelSerializer):
    class Meta:
        model = players
        fields = '__all__'
      
 