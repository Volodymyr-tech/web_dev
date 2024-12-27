from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Categories, Lead
from catalog.forms import ProductForm, LeadForm


class MainPageView(ListView):
    model = Product
    template_name = 'html_pages/main_page.html'
    context_object_name = 'products'
    paginate_by = 6



class CategoriesListView(ListView):
    '''Класс вывода страницы Каталог'''
    model = Categories  # Модель для отображения
    template_name = "html_pages/categories.html"  # Путь к шаблону
    context_object_name = "categories"  # Название переменной в шаблоне


class LeadCreateView(CreateView):
    form_class = LeadForm  # Указываем форму
    template_name = 'html_pages/contact.html'  # Шаблон для рендеринга
    success_url = '/catalog/'  # Куда перенаправлять после успешного сохранения



class ProductDetailView(DetailView):
    model = Product
    template_name = 'html_pages/product_details.html'
    context_object_name = 'product'


class AddProductView(CreateView):
    form_class = ProductForm
    template_name = 'html_pages/add_product_form.html'
    success_url = reverse_lazy("catalog:home")  # Переход на страницу каталога после добавления продукта


#def product_search(request):
#    query = request.GET.get('query', '')  # Получаем строку поиска из запроса
#    results = Product.objects.filter(description__icontains=query) if query else []  # Фильтруем по описанию
#    return render(request, 'product_search_results.html', {'query': query, 'results': results})





#def main_page(request):
 ##  products = Product.objects.all()  # Получение списка товаров из модели
   # paginator = Paginator(products, 9)  # 9 товаров на странице
#
 #   page_number = request.GET.get('page')  # Получение текущей страницы из запроса
  #  page_obj = paginator.get_page(page_number)  # Текущая страница

   # return render(request, "html_pages/main_page.html", {'page_obj': page_obj})


#def show_categories(request):
 #   '''Функиция вывода страницы Каталог'''
 #   categories = Categories.objects.all()
#    context = {
#        "categories":categories
#    }
#    if request.method == "GET":
#        return render(request, "html_pages/categories.html", context)



#def show_category(request):
 #   '''Функиция вывода страницы Категории'''
  #  if request.method == "GET":
   #     return render(request, 'html_pages/category.html')



#def product_detail(request, pk):
#    product = Product.objects.get(pk=pk)
#    context = {
#        "product":product
#    }
#    return render(request, "html_pages/product_details.html", context)



#def add_product(request):
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