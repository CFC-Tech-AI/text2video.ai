from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),   
    path('text_to_video/', text_to_video, name='text_to_video'),
      
]