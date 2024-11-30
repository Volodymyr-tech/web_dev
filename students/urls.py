from tkinter.font import names

from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("main_page/", views.main_page, name="main_page"),
    path("catalog/", views.show_catalog, name="show_catalog"),
    path("contact/", views.contact, name="contact"),
    path("category/", views.show_category, name="category")
]

