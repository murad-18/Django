from django.urls import path
from . import views
urlpatterns = [
    path("", views.welcome, name="Home Page"),
    path("Aboutus", views.aboutus, name="About us"),
    path("Contactus", views.contactus, name="Contact us"),
    path("GenerateNumber", views.generateNum, name="Generate Number")
]
