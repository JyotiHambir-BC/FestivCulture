from django.urls import path
from . import views

urlpatterns = [

    path('', views.AllFestivals.as_view(), name="festivals"),
    path("like/<slug:slug>/", views.PostLike.as_view(), name="post_like"),
    path('favourite/', views.view_favourite_list, name='view_favourite_list'),
    path('favourite/<slug:slug>', views.favourite_list, name='favourite_list'),
    path('<slug:slug>/', views.details_post, name='details_post'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit,
        name='comment_edit'
    ),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),

]
