from django.contrib import admin

from blog.models import BlogPost


# Register your models here.
@admin.register(BlogPost)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "views")
    list_filter = ("created_at",)
    search_fields = ("title",)
from django.contrib import admin

# Register your models here.