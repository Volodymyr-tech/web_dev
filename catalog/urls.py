from tkinter.font import names

from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.main_page, name="home"),
    path("catalog/", views.show_catalog, name="show_catalog"),
    path("contacts/", views.contact, name="contacts"),
    path("category/", views.show_category, name="category")
]

