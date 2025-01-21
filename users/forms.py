from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import BooleanField

from users.models import CustomUser


class StyleProductMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CustomUserCreationForm(StyleProductMixin, UserCreationForm):
    username = forms.CharField(max_length=50, required=True)

    class Meta:
        model = CustomUser
        fields = (
            "email",
            "username",
            "phone_number",
            "password1",
            "password2",
            "avatar",
            "country",
        )


    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone_number


class UserEditForm(StyleProductMixin, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("email", "phone_number", "avatar")
