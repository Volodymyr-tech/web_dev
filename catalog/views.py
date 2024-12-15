from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from catalog.models import Product, Categories
from catalog.templatetags.forms import ProductForm


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


def add_product(request):
        # if this is a POST request we need to process the form data
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = ProductForm(request.POST, request.FILES)
            # check whether it's valid:
            if form.is_valid(): # если проверка вернет тру проверенные данные формы окажутся в словаре form.cleaned_data
                form.save()
                # redirect to a new URL:
                return redirect("catalog:home")

        # if a GET (or any other method) we'll create a blank form
        else:
            form = ProductForm()

        return render(request, "html_pages/add_product_form.html", {"form": form})
