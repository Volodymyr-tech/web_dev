from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from users.models import CustomUser


# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'username', 'phone_number', 'password1', 'password2']

        #widgets ={

      #  }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number
# Форма авторизации

class CustomAuthenticationForm(AuthenticationForm):
    pass