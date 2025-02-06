from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from catalog.forms import LeadForm, ProductForm, ModerForm
from catalog.models import Categories, Product
from config.services import CacheService
from config import settings


class MainPageView(ListView):
    """Класс для просмотра списка продуктов"""

    model = Product
    template_name = "html_pages/main_page.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(status="published")


class CategoriesListView(ListView):
    """Класс вывода страницы Каталог"""

    model = Categories  # Модель для отображения
    template_name = "html_pages/categories.html"  # Путь к шаблону
    context_object_name = "categories"  # Название переменной в шаблоне


    def get_queryset(self):
        return CacheService.get_cached_obj_or_objects("catalog", self.model.__name__, None)


class CategoryDetailView(DetailView):
    '''Класс для детального просмотра категории'''
    model = Categories  # Модель для отображения
    template_name = "html_pages/categories_details.html"
    context_object_name = "category"


class CategoryDeleteView(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    model = Categories  # Модель для отображения
    template_name = "html_pages/delete_category.html"
    context_object_name = "category"
    success_url = reverse_lazy("catalog:home")



class LeadCreateView(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    """Класс для создания контактной формы. При отправке завяки приходит оповещение на почту"""

    form_class = LeadForm  # Указываем форму
    template_name = "html_pages/contact.html"  # Шаблон для рендеринга
    success_url = "/catalog/"  # Куда перенаправлять после успешного сохранения

    def form_valid(self, form):
        # Сохраняем объект, но не перенаправляем
        response = super().form_valid(form)

        # Вызываем метод отправки уведомления
        self.notification()
        return response

    def notification(self):
        send_mail(
            "Новая заявка",
            f"На сайте {self.request.get_host()} была получена новая заявка от: {self.object.name} - {self.object.email}",
            settings.EMAIL_HOST_USER,
            ["tvoitarget.info@gmail.com"],
            fail_silently=False,  # Отключаем отправку писем с ошибками
        )

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    """Класс для детального просмотра продукта"""

    model = Product
    template_name = "html_pages/product_details.html"
    context_object_name = "product"



class AddProductView(LoginRequiredMixin, CreateView, PermissionRequiredMixin):
    """Класс для создания продукта"""

    form_class = ProductForm
    template_name = "html_pages/add_product_form.html"
    success_url = reverse_lazy(
        "catalog:home"
    )  # Переход на страницу каталога после добавления продукта

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductSearchView(ListView):
    """Класс для поиска продукта"""

    model = Product
    template_name = "html_pages/product_search_results.html"
    context_object_name = "products"

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            return Product.objects.filter(
                name__icontains=query
            )  # Поиск по названию продукта
        return Product.objects.all()


class ProductUpdateView(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    """Класс для изменения продукта"""

    model = Product
    form_class = ProductForm
    template_name = "html_pages/update_product_form.html"
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product') and user.has_perm('catalog.delete_product'):
            return ModerForm
        raise PermissionDenied("Нет прав на изменение или удаление продукта")


class ProductDeleteView(LoginRequiredMixin, DeleteView, PermissionRequiredMixin):
    """Класс для удаления продукта"""

    model = Product
    template_name = "html_pages/delete_product_confirm.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:home")
    permission_required = 'catalog.delete_product'

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        user = self.request.user

        if product.owner == user or user.has_perm('catalog.delete_product'):
            return product

        raise PermissionDenied('Нет прав на удаление продукта')


class CanUnpublishView(LoginRequiredMixin, UpdateView, PermissionRequiredMixin):
    """Класс для сняти публичности продукта"""
    model = Product
    form_class = ModerForm
    template_name = "html_pages/update_product_form.html"
    success_url = reverse_lazy("catalog:home")
    permission_required = 'catalog.can_unpublish_product'

    def form_valid(self, form):
        pass




# def main_page(request):
##  products = Product.objects.all()  # Получение списка товаров из модели
# paginator = Paginator(products, 9)  # 9 товаров на странице
#
#   page_number = request.GET.get('page')  # Получение текущей страницы из запроса
#  page_obj = paginator.get_page(page_number)  # Текущая страница

# return render(request, "html_pages/main_page.html", {'page_obj': page_obj})


# def show_categories(request):
#   '''Функиция вывода страницы Каталог'''
#   categories = Categories.objects.all()
#    context = {
#        "categories":categories
#    }
#    if request.method == "GET":
#        return render(request, "html_pages/categories.html", context)


# def show_category(request):
#   '''Функиция вывода страницы Категории'''
#  if request.method == "GET":
#     return render(request, 'html_pages/category.html')


# def product_detail(request, pk):
#    product = Product.objects.get(pk=pk)
#    context = {
#        "product":product
#    }
#    return render(request, "html_pages/product_details.html", context)


# def add_product(request):
# if this is a POST request we need to process the form data
#       if request.method == "POST":
# create a form instance and populate it with data from the request:
#           form = ProductForm(request.POST, request.FILES)
# check whether it's valid:
#            if form.is_valid(): # если проверка вернет тру проверенные данные формы окажутся в словаре form.cleaned_data
#                form.save()
# redirect to a new URL:
#               return redirect("catalog:home")

# if a GET (or any other method) we'll create a blank form
#        else:
#            form = ProductForm()

#       return render(request, "html_pages/add_product_form.html", {"form": form})


# def contact(request):
#   '''Функиция вывода страницы Контакты и отправка POST запроса в форме'''
#    if request.method == 'POST':
#       # Получение данных из формы
#        name = request.POST.get('name')
#       email = request.POST.get('email')
#        message = request.POST.get('message')
#       return HttpResponse (f"{name} твоя заявка отправлена. Проверь почту {email}.\nСообщение: {message}")
#   return render(request, 'html_pages/contact.html')
