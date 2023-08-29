from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("list/<int:list_id>", views.ItemView.as_view(), name="list")
]
