from users.models import players
from .models import * 
from rest_framework import serializers
 

# -------------------------------------------- REGISTRATION MODELS------------------------------------------ #
class SportsSer(serializers.ModelSerializer):
    class Meta:
        model = sports
        fields = '__all__'
      
 