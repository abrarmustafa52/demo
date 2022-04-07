# django 
from django.urls import *
from django.contrib import * 

# app level 
from .views import *   


class ApiUrls():
    def getUrls():
        urlpatterns = [ 
            path('nplayers', SportsViewNPlayers.as_view()),  
            path('noplayers', SportsViewNoPlayers.as_view()),    
        ]
        return urlpatterns
        
        