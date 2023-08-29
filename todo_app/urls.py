from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("list/<int:list_id>", views.ItemView.as_view(), name="list"),
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    path("list/<int:list_id>/item/add/",
         views.TodoCreate.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>/",
         views.TodoUpdate.as_view(), name="item-update"),
]
