from django.urls import path
from . import views
from .views import CART,homepage

urlpatterns = [
    path("login", views.index, name = "login-page"),
    path("homepage", homepage.as_view(), name = "home-page"),
    path("signin", views.signin, name="signin-page"),
    path("cart",CART.as_view(), name="cart")
]