
from django.urls import path
from .views import BlogListView, AddBlogFormView, BlogDetailView

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("add-article/", AddBlogFormView.as_view(), name="add-article"),
    path("detail/<slug:slug>/", BlogDetailView.as_view(), name="detail"),
]
