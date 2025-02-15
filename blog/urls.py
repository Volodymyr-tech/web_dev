from django.urls import path

from .views import (AddBlogFormView, BlogDetailView, BlogListView,
                    DeleteBlogView, UpdateBlogView)

app_name = "blog"


urlpatterns = [
    path("", BlogListView.as_view(), name="blog"),
    path("add-article/", AddBlogFormView.as_view(), name="add-article"),
    path("detail/<slug:slug>/", BlogDetailView.as_view(), name="detail"),
    path("update/<slug:slug>/", UpdateBlogView.as_view(), name="update"),
    path("delete/<slug:slug>/", DeleteBlogView.as_view(), name="delete"),
]
