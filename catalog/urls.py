

from django.urls import path

from .views import MainPageView, CategoriesListView, ProductDetailView, AddProductView, LeadCreateView, \
    ProductSearchView, ProductUpdateView, ProductDeleteView, CategoriesDetailView

app_name = "catalog"

urlpatterns = [
    path("", MainPageView.as_view(), name="home"),
    path('contact/', LeadCreateView.as_view(), name='contact'),
    path("categories/", CategoriesListView.as_view(), name="categories"),
    path('category-detail/<str:pk>', CategoriesDetailView.as_view(), name="category-detail"),
    path("add-product/",AddProductView.as_view(), name="add_product_form"),
    path('delete-product/<int:pk>',ProductDeleteView.as_view(), name='delete-product'),
    path('update-product/<int:pk>', ProductUpdateView.as_view(), name="update-product"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path('search/', ProductSearchView.as_view(), name='product_search'),
]

