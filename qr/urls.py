from django.conf import settings
from django.contrib import admin
from django.urls import path
from.views import qrurl,textqr


urlpatterns = [
    path('',qrurl,name="qrurl"),
    
    path('text/',textqr,name="textqr"),
   
    
]