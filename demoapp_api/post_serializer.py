
from rest_framework import serializers
   
# POST  
 
class PostOtpSerializer(serializers.Serializer):  
    loginid         = serializers.CharField(required=True)
    otpType         = serializers.CharField(required=True)

class PostVerifyOtpSerializer(serializers.Serializer):  
    loginid         = serializers.CharField(required=True)
    otpCode         = serializers.CharField(required=True)
  
class PostAccountSerializer(serializers.Serializer): 
    loginid         = serializers.CharField(required=True)
    account_type    = serializers.CharField(required=True)
    pin             = serializers.CharField(required=True)
    deviceType      = serializers.CharField(required=False) 
    fcmToken        = serializers.CharField(required=False)
 
class PostDeliveryAddressSerializer(serializers.Serializer):  
    address         = serializers.CharField(required=True)
    city            = serializers.CharField(required=True) 
    lat             = serializers.FloatField(required=True)
    lon             = serializers.FloatField(required=True)
 
class PostSignInSerializer(serializers.Serializer): 
    loginid         = serializers.CharField(required=True)
    pin             = serializers.CharField(required=False)
    
# PUT

class PutAccountSerializer(serializers.Serializer):  
    fullname        = serializers.CharField(required=True)  

class PutDeliveryAddressSerializer(serializers.Serializer):  
    addressId       = serializers.IntegerField(required=True)
    address         = serializers.CharField(required=True)
    city            = serializers.CharField(required=True) 
    lat             = serializers.FloatField(required=True)
    lon             = serializers.FloatField(required=True)

 
# DELETE
class DeleteDeliveryAddressSerializer(serializers.Serializer):  
    addressId       = serializers.IntegerField(required=True)
 