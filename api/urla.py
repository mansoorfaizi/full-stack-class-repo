from django.urls import path
from .views import showMessage

urlpatterns = [
   path('message/', showMessage, name='message') 
]