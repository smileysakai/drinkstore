from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("<int:drink_id>", views.drink, name="drink"),
    path("<int:drink_id>/add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("view_cart", views.view_cart, name="view_cart"),
    path("view_cart/delete/<int:drink_id>",views.delete_cartitem, name="delete_cartitem"),
    path("view_cart/update/<int:drink_id>",views.update_cartitem, name="update_cartitem")
] 