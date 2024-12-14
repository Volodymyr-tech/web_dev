from tkinter.font import names

from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.main_page, name="home"),
    path("products/", views.main_page, name="products"),
    path("contact/", views.contact, name="contact"),
    path("categories/", views.show_categories, name="categories"),
    #path("base/", , name="base"),
    path("product/<str:pk>/", views.product_detail, name="product"),
]

