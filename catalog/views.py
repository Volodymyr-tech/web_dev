from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from catalog.models import Product


def main_page(request):
    '''Функиция вывода главной страницы'''
    if request.method == "GET":
        return render(request, "html_pages/main_page.html")

def show_catalog(request):
    '''Функиция вывода страницы Каталог'''
    if request.method == "GET":
        return render(request, "html_pages/catalog.html")

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

def show_products(request):
    product = Product.objects.all()
    context = {
        "product" : product
    }
    return render(request, "html_pages/product_list.html", context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        "product":product
    }
    return render(request, "html_pages/product_details.html", context)