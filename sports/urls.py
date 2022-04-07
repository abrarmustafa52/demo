# django 
from django.urls import *
from django.contrib import * 

# app level 
from ..demoapp_api.views import *   


class ApiUrls():
    def getUrls():
        urlpatterns = [ 
            path('content', TableOfContentView.as_view()),    
        ]
        return urlpatterns
        
        