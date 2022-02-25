
from rest_framework import serializers
   
# POST  
 
class PutUserSerializer(serializers.Serializer):  
    fullname           = serializers.CharField(required=True)
    # password          = serializers.CharField(required=True)
 