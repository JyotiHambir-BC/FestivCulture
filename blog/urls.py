from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.AllFestivals.as_view(), name="festivals"),
]