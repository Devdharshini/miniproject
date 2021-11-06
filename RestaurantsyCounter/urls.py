from django.urls import path
from . import views
from .views import homepage,delivered

urlpatterns=[
    path("login", views.index, name = "loginpage"),
    path("homepage", homepage.as_view(), name="homepage"),
    path("delivered", delivered.as_view(), name="delivered"),
    path("delivers", views.delivers, name="delivers")
]