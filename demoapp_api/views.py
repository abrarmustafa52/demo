import json
import random
import datetime 


from django.db.models import Q
from django.core import * 
from django.shortcuts import *
from django.contrib.gis.geos import *
from rest_framework.response import * 
from rest_framework.permissions import *    
from rest_framework.authentication import * 
from rest_framework.authtoken.models import *  


# Create your views here.   


class Categories(APIView):
 
    def get(self, request):
     
        try: 
            _categories = CategoryModel.objects.all() 
            categoriesresponce = CategorySerializer(_categories, many=True) 
            data=categoriesresponce.data
            msg=SUCCESS
            isSuccess=True 

        except:
            data=None
            msg="failed while fetching categories" 
            isSuccess=False 
        return Response({"data": data, "msg": msg, "issuccess": isSuccess}) 

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        ser = N_PostCategorySerializer(data=request.data)
         
        if ser.is_valid():
            
            if not request.user.is_superuser:
                msg="not have admin level permissions" 
                isSuccess=False  
            else:
                try: 
                    _category = CategoryModel(title=ser.validated_data["title"])
                    _category.image = ser.validated_data["image"]   
                    _category.save()
                    msg=SUCCESS
                    isSuccess=True 
    
                except:
                    msg="error while adding category" 
                    isSuccess=False  
        else : 
            msg=ser.errors 
            isSuccess=False  
         
        return Response({"data": None, "msg": msg, "issuccess": isSuccess}) 
  

    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,) 
    def put(self, request):
        ser = N_PutCategorySerializer(data=request.data)
         
        if ser.is_valid():
            
            if not request.user.is_superuser:
                msg="not have admin level permissions" 
                isSuccess=False  
            else:
                try: 
                    category = CategoryModel.objects.get(id=ser.validated_data["categoryId"])
                    category.title = ser.validated_data["title"]
                    category.image = ser.validated_data["image"]
                    category.save()  
                    msg=SUCCESS
                    isSuccess=True  

                except:
                    msg="error while updating category" 
                    isSuccess=False 
                        
                  
        else : 
            msg=ser.errors 
            isSuccess=False  
         
        return Response({"data": None, "msg": msg, "issuccess": isSuccess}) 
 
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    def delete(self, request):
        ser = N_DeleteCategorySerializer(data=request.data)
         
        if ser.is_valid()  :
            if not request.user.is_superuser:
                msg="not have admin level permissions" 
                isSuccess=False  
            else:
                try: 
                    _category = CategoryModel.objects.get(id=ser.validated_data["categoryId"])
                    _category.delete()  
                    msg=SUCCESS
                    isSuccess=True  
                except:
                    msg="error while deleting category" 
                    isSuccess=False  
        else : 
            msg=ser.errors 
            isSuccess=False  
         
        return Response({"data": None, "msg": msg, "issuccess": isSuccess}) 
  
   
