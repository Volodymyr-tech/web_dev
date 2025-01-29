from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from dotenv import load_dotenv

from config import settings

load_dotenv()

from django.core.mail import send_mail
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogListView(ListView):
    queryset = BlogPost.objects.filter(status=BlogPost.PUBLISHED).order_by(
        "-created_at"
    )  # Сортируем по дате создания, от новых к старым
    template_name = "blog/blog_list.html"  # Путь к шаблону
    context_object_name = "blog"  # Контекстное имя для переменной в шаблоне
    extra_context = {
        "popular_posts": BlogPost.objects.filter(status=BlogPost.PUBLISHED).order_by(
            "-views"
        )[:2]
    }  # Выводим 2 самых популярных статей


class AddBlogFormView(CreateView, PermissionRequiredMixin, LoginRequiredMixin):
    form_class = BlogPostForm
    template_name = "blog/add_blog_form.html"
    success_url = reverse_lazy(
        "blog:blog"
    )  # Перенаправляем на страницу блога после успешного создания

    def form_valid(self, form):
        # Сохраняем объект, но не перенаправляем
        response = super().form_valid(form)

        # Вызываем метод отправки уведомления
        self.notification()
        return response

    def notification(self):
        send_mail(
            "Новая статья",
            f"На сайте {self.request.get_host()} была добавлена новая статья: {self.object.title}",
            settings.EMAIL_HOST_USER,
            ["tvoitarget.info@gmail.com"],
            fail_silently=False,  # Отключаем отправку писем с ошибками
        )


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "blog_post"
    slug_field = "slug"  # Указываем поле для поиска
    slug_url_kwarg = "slug"  # Указываем имя переменной в URL

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1  # Увеличиваем число просмотров
        self.object.save()
        return self.object


class DeleteBlogView(DeleteView, PermissionRequiredMixin, LoginRequiredMixin):
    model = BlogPost
    success_url = reverse_lazy("blog:blog")
    template_name = "blog/delete_blog_confirm.html"
    context_object_name = "blog_post"


class UpdateBlogView(UpdateView, PermissionRequiredMixin, LoginRequiredMixin):
    model = BlogPost
    template_name = "blog/update_blog_form.html"
    form_class = BlogPostForm
    context_object_name = "blog_post"

    def get_success_url(self):
        return reverse_lazy("blog:detail", kwargs={"slug": self.object.slug})


