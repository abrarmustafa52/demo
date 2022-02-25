import json
import random
import datetime 


from django.db.models import Q
from demoapp_api.models import *
from utils.consts import * 
from demoapp_api.models import *
from demoapp_api.post_serializer import *
from demoapp_api.serializers import *
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


class TableOfContentView(APIView):
 
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    def get(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try: 
            _content = TableOfContentModel.objects.all() 
            data = TableOfContentSer(_content, many=True) .data
            msg=SUCCESS
            isSuccess=True 

        except Exception as ex:
            data=None
            msg="failed while fetching table of content "+str(ex) 
            isSuccess=False 
        return Response({"data": data, "msg": msg, "issuccess": isSuccess}) 

   
    authentication_classes = [TokenAuthentication]
    permission_classes = [SAFE_METHOD_Permission]
    def post(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try:
            ser = PostTableOfContentSer(data=request.data)
            if not ser.is_valid(): 
                msg=ser.errors
                raise Exception('My error!')

            _tableContent = TableOfContentModel(description=ser.validated_data["description"])
            if ser.validated_data["parentcontent_id"]:
                _tableContent.parent_section =  TableOfContentModel.objects.get(id=ser.validated_data["parentcontent_id"])
            _tableContent.save() 
            msg=SUCCESS
            isSuccess=True  
    
        except Exception as ex:
            data=None
            msg="failed while adding table of content "+str(ex) 
            isSuccess=False 
        return Response({"data": data, "msg": msg, "issuccess": isSuccess}) 

    authentication_classes = [TokenAuthentication]
    permission_classes = [SAFE_METHOD_Permission]
    def put(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try:
            ser = PutTableOfContentSer(data=request.data)
            if not ser.is_valid(): 
                msg=ser.errors
                raise Exception('My error!')

            _tableContent = TableOfContentModel.objects.get(id=ser.validated_data["table_id"])
            _tableContent.description = ser.validated_data["description"]
            if ser.validated_data["parentcontent_id"]:
                _tableContent.parent_section =  TableOfContentModel.objects.get(id=ser.validated_data["parentcontent_id"])
            _tableContent.save() 
            msg=SUCCESS
            isSuccess=True  
    
        except Exception as ex:
            data=None
            msg="failed while updating table of content "+str(ex) 
            isSuccess=False 
        return Response({"data": data, "msg": msg, "issuccess": isSuccess}) 
