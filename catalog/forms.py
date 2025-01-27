from django import forms
from catalog.models import Product, Categories, Lead
from .validators import validate_no_forbidden_words


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        empty_label="Категория не выбрана",
        label="Категория продукта",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Product
        fields = ["name", "category", "description", "image", "purchase_price"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "purchase_price": forms.NumberInput(attrs={"class": "form-control"}),
        }

        # Подключаем валидаторы

    def clean_name(self):
        name = self.cleaned_data.get("name")
        validate_no_forbidden_words(name)  # Проверяем запрещённые слова
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        validate_no_forbidden_words(description)  # Проверяем запрещённые слова
        return description

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get("purchase_price")
        if purchase_price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return purchase_price

    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            if not image.name.lower().endswith(('.jpeg', '.png', '.jpg')):
                raise forms.ValidationError('Фото неверного формата')

            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError('Фото не должно превышать 5 МБ')

        return image


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["name", "email", "phone", "message", "checkbox"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите имя"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Введите email"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите телефон"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Введите сообщение",
                }
            ),
            "checkbox": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
