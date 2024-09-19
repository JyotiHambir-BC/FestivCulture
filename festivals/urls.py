from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.festivals, name='festivals'),
]