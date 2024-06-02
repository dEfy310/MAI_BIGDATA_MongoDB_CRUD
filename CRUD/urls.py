from django.urls import path
from . import views

urlpatterns = [
    path("", views.restaurants, name="restaurants"),
    path("create/", views.createRestaurant, name="createRestaurant"),
    path("edit/<str:Name>", views.editRestaurant, name="editRestaurant"),
    path("delete/<str:Name>", views.deleteRestaurant, name="deleteRestaurant"),
]