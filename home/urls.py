from django.urls import path
from home import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about),
    path('create-post/', views.create_post,name="create_post"),
]