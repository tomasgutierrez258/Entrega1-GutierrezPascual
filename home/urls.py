from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create-post/', views.create_post,name="create_post"),
    path('edit-post/<int:pk>/', views.EditPost.as_view(),name="edit_post"),
    path('remove-post/<int:pk>/', views.RemovePost.as_view(),name="remove_post"),
    
    path('about/', views.about),
]