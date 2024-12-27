from django import forms
from catalog.models import Product, Categories, Lead


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label="Категория не выбрана",
                                      label='Категория продукта', widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = Product
        fields = ["name", "category", "description", "image", "purchase_price"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "purchase_price": forms.NumberInput(attrs={"class": "form-control"}),
        }

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'message', 'checkbox']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите телефон'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите сообщение'}),
            'checkbox': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }