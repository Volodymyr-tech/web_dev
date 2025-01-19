from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from users.models import CustomUser


# Форма регистрации
class StyleProductMixin:
    pass


class CustomUserCreationForm(StyleProductMixin,UserCreationForm):
    username = forms.CharField(max_length=50, required=True)


    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'phone_number', 'password1', 'password2', 'avatar', 'country')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number
# Форма авторизации

class CustomAuthenticationForm(AuthenticationForm):
    pass


class StyleProductMixin:
    pass


class UserEditForm(StyleProductMixin, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "phone_number", "avatar")