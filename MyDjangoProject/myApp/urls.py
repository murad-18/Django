from django.urls import path
from . import views
urlpatterns = [
    path("Home", views.welcome, name="Home Page"),
    path("Aboutus", views.aboutus, name="About us"),
    path("Contactus", views.contactus, name="Contact us"),
    path("GenerateNumber", views.generateNum, name="Generate Number"),
    path("Signup", views.signup_view, name="Signup Page"),
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
]
