from django.urls import path

from .views import (AddProductView, CategoriesListView, LeadCreateView,
                    MainPageView, ProductDeleteView, ProductDetailView,
                    ProductSearchView, ProductUpdateView,
                    CategoryDetailView, CategoryDeleteView, ProductsByCategoryView)

app_name = "catalog"

urlpatterns = [
    path("", MainPageView.as_view(), name="home"),
    path("contact/", LeadCreateView.as_view(), name="contact"),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path('category-detail/<int:pk>', CategoryDetailView.as_view(), name="category-detail"),
    path('category-delete/<int:pk>', CategoryDeleteView.as_view(), name="category-delete"),
    path("add-product/", AddProductView.as_view(), name="add_product_form"),
    path("delete-product/<int:pk>", ProductDeleteView.as_view(), name="delete-product"),
    path("update-product/<int:pk>", ProductUpdateView.as_view(), name="update-product"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("search/", ProductSearchView.as_view(), name="product_search"),
    path("products_by_category/<int:pk>", ProductsByCategoryView.as_view(), name="products_by_category"),
]
