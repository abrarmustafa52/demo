# django 
from django.urls import *
from django.contrib import * 

# app level 
from .views import *   


class UserUrls():
    def getUrls():
        urlpatterns = [ 
            path('user', UserView.as_view()),    
        ]
        return urlpatterns
        
        