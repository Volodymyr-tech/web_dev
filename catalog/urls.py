from tkinter.font import names

from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.main_page, name="home"),
    path("products/", views.show_products, name="products"),
    path("contacts/", views.contact, name="contacts"),
    path("category/", views.show_category, name="category"),
    #path("base/", , name="base"),
    path("product/<str:pk>/", views.product_detail, name="product"),
]

