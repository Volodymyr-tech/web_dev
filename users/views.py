import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import CustomUserCreationForm, UserEditForm, UserLoginForm
from users.models import CustomUser


# Create your views here.
class RegisterView(CreateView):
    '''Класс для регистрации нового юзера'''
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


    def form_valid(self, form):
        '''Метод для валидации формы и отправки эл.почты с токеном для подтвердения аккаунта'''
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-verification/{token}/"
        send_mail(
            subject="Confirmation for registration",
            message=f"Go through the link to confirm your registration {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    '''Подтверждение аккаута и сохранение в БД'''
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse_lazy("users:login"))


class UpdateCustomUser(LoginRequiredMixin, UpdateView):
    '''Класс для редактирования профиля пользователя'''
    model = CustomUser
    form_class = UserEditForm
    template_name = "users/update_user_form.html"
    success_url = reverse_lazy("catalog:home")


class UserLoginView(LoginView):
    '''Класс для входа в веб приложение'''
    form_class = UserLoginForm
    template_name = "login.html"


