from django.db import models
from django.utils.text import slugify


# Create your models here.
class BlogPost(models.Model):
    PUBLISHED = "Опубликовано"  # данные поля отображаются в БД
    IN_WORK = "В работе"
    DELETED = "Удалено"

    STATUS_CHOICES = [
        (PUBLISHED, "Опубликовано"),  # данные поля отображаются в админке Django
        (IN_WORK, "В работе"),
        (DELETED, "Удалено"),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True, max_length=255, db_index=True, verbose_name="Slug", blank=True
    )
    content = models.TextField(verbose_name="Содержимое поста")
    image = models.ImageField(
        upload_to="blog/", verbose_name="Изображение", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=STATUS_CHOICES,
        verbose_name="Статус публикации",
        default=IN_WORK,
        blank=True,
    )
    views = models.IntegerField(default=0, null=True)

    class Meta:
        verbose_name = "Статья блога"
        verbose_name_plural = "Статьи блога"
        ordering = ["-created_at"]


    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
