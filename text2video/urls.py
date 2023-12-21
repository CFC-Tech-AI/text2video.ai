from django.urls import path
from .views import *

urlpatterns = [
     
    path('', text_to_video, name='text_to_video'),
      
]