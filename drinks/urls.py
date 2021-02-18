from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("<int:drink_id>", views.drink, name="drink")  
] 