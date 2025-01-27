from tkinter.font import names

from django.urls import path
from . import views
from .views import MainPageView, CategoriesListView, ProductDetailView, AddProductView, LeadCreateView

app_name = "catalog"

urlpatterns = [
    path("", MainPageView.as_view(), name="home"),
    path('contact/', LeadCreateView.as_view(), name='contact'),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path("add-product/",AddProductView.as_view(), name="add_product_form"),
    path("product/<str:pk>/", ProductDetailView.as_view(), name="product"),
    #path('search/', views.product_search, name='product_search'),
]

