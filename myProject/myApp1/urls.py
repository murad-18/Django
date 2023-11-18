from django.urls import path
from . import views
urlpatterns = [
    path("", views.welcome, name="Home Page"),
    path("Form", views.form, name="Form Page"),
]
