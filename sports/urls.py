# django 
from django.urls import *
from django.contrib import * 

# app level 
from .views import *   


class ApiUrls():
    def getUrls():
        urlpatterns = [ 
            path('content', SportsView.as_view()),    
        ]
        return urlpatterns
        
        