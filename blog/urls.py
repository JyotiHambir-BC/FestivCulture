from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.AllFestivals.as_view(), name="festivals"),
    path('<slug:slug>/', views.details_post, name='post_details'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
     path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]