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
 
#  apis are already very fast
# Create your views here.

class UserView(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    def get(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try: 
            _players = players.objects.all() 
            data = UserSer(_players, many=True) .data
            msg=SUCCESS
            isSuccess=True 

        except Exception as ex:
            data=None
            msg="failed while fetching users"+str(ex) 
            isSuccess=False 
        return Response({"data": data, "msg": msg, "issuccess": isSuccess}) 
 