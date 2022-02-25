import json
import random
import datetime 


from django.db.models import Q
from users.models import UserModel
from utils.consts import * 
from users.models import *
from users.put_serializer import *
from users.serializers import UserSer
from utils.permission import * 


from django.db.models import Q
from django.core import * 
from django.shortcuts import *
from rest_framework.views import * 
from django.contrib.gis.geos import *
from rest_framework.response import * 
from rest_framework.permissions import *   
from django.contrib.auth.hashers import *  
from rest_framework.authentication import * 
from rest_framework.authtoken.models import *  
 
# Create your views here.   


# Create your views here.

class UserView(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    def get(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try: 
            _users = UserModel.objects.all() 
            data = UserSer(_users, many=True) .data
            msg=SUCCESS
            isSuccess=True 

        except Exception as ex:
            data=None
            msg="failed while fetching users"+str(ex) 
            isSuccess=False 
        return Response({"data": data, "msg": msg, "issuccess": isSuccess}) 

    
    authentication_classes = [TokenAuthentication]
    permission_classes = [SAFE_METHOD_Permission]
    def put(self, request):
        ser = PutUserSerializer(data=request.data)
         
        if ser.is_valid():
            
            if not request.user.is_superuser:
                msg="not have admin level permissions" 
                isSuccess=False  
            else:
                try: 
                    request.user.fullname = ser.validated_data["fullname"]
                    request.user.save()  
                    msg=SUCCESS
                    isSuccess=True  

                except:
                    msg="error while updating user" 
                    isSuccess=False 
                        
                  
        else : 
            msg=ser.errors 
            isSuccess=False  
         
        return Response({"data": None, "msg": msg, "issuccess": isSuccess}) 

 