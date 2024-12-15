from tkinter.font import names

from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.main_page, name="home"),
    path("contact/", views.contact, name="contact"),
    path("categories/", views.show_categories, name="categories"),
    path("add-product/",views.add_product , name="add_product_form"),
    path("product/<str:pk>/", views.product_detail, name="product"),
]

