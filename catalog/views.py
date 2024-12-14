from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from catalog.models import Product, Categories


def main_page(request):
    '''Функиция вывода главной страницы'''
    products = Product.objects.all()  # Получение списка товаров из модели
    paginator = Paginator(products, 9)  # 9 товаров на странице

    page_number = request.GET.get('page')  # Получение текущей страницы из запроса
    page_obj = paginator.get_page(page_number)  # Текущая страница

    return render(request, "html_pages/main_page.html", {'page_obj': page_obj})


def show_categories(request):
    '''Функиция вывода страницы Каталог'''
    categories = Categories.objects.all()
    context = {
        "categories":categories
    }
    if request.method == "GET":
        return render(request, "html_pages/categories.html", context)

def contact(request):
    '''Функиция вывода страницы Контакты и отправка POST запроса в форме'''
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse (f"{name} твоя заявка отправлена. Проверь почту {email}.\nСообщение: {message}")
    return render(request, 'html_pages/contact.html')


def show_category(request):
    '''Функиция вывода страницы Категории'''
    if request.method == "GET":
        return render(request, 'html_pages/category.html')



def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        "product":product
    }
    return render(request, "html_pages/product_details.html", context)