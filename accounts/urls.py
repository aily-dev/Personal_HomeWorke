from django.urls import path
from . import views

urlpatterns = [
    path("getprods/", views.get_products),
]
