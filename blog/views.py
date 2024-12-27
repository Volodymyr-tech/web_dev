from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogListView(ListView):
    queryset = BlogPost.objects.order_by('-created_at')# Сортируем по дате создания, от новых к старым
    template_name = 'blog/blog_list.html' # Путь к шаблону
    context_object_name = 'blog' # Контекстное имя для переменной в шаблоне


class AddBlogFormView(CreateView):
    form_class = BlogPostForm
    template_name = 'blog/add_blog_form.html'
    success_url = reverse_lazy('blog:blog')# Перенаправляем на страницу блога после успешного создания


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog_post'
    slug_field = 'slug'  # Указываем поле для поиска
    slug_url_kwarg = 'slug'  # Указываем имя переменной в URL

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1  # Увеличиваем число просмотров
        self.object.save()
        return self.object


class DeleteBlogView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blog')
    template_name = 'blog/delete_blog_confirm.html'
    context_object_name = 'blog_post'


class UpdateBlogView(UpdateView):
    model = BlogPost
    template_name = 'blog/update_blog_form.html'
    form_class = BlogPostForm
    context_object_name = 'blog_post'

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'slug': self.object.slug})
