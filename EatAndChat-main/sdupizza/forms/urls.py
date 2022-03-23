from django.urls import path
from . import views
urlpatterns = [
    path('form/', views.index, name="form"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.main, name="main"),
    path('basket/', views.basket, name="basket"),
    path('update_item/', views.updateitem, name="update_item"),
    path('register/', views.registerPage, name='register'),
    path('user/', views.UserPage, name='user-page')
]
