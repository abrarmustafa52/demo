from .models import * 
from rest_framework import serializers
 

# -------------------------------------------- REGISTRATION MODELS------------------------------------------ #
class UserSer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["email","createdAt"]
      
 