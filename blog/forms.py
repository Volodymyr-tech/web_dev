from django import forms
from django.utils.text import slugify

from .models import BlogPost

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost  # Указываем модель
        fields = ['title', 'slug', 'content', 'image', 'status']  # Поля, которые включаем в форму
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите текст поста'}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите слаг'})
         }