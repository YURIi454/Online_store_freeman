import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import CustomUser


class DetailUserView(View):
    """ Подробная информация о пользователе. """

    model = CustomUser
    template_name = "your_profile.html"


class RegisterUserView(CreateView):
    """ Регистрация нового пользователя. """

    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        """ Отправка письма пользователю. """

        subject = ""
        message = ""
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email, ]
        send_mail(subject, message, from_email, recipient_list)


class UpdateUserView(LoginRequiredMixin, UpdateView):
    """ Редактирование данных зарегистрированного пользователя. """

    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'update_user.html'
    success_url = reverse_lazy('catalog:main')

    def get_object(self):
        return self.request.user


class DeleteUserView(View):
    """ Удаление информации о пользователе. """

    form_class = CustomUserCreationForm
    template_name = 'delete_user.html'
    success_url = reverse_lazy('main')


def email_verification(request, token):
    """ Верификация пользователя. """

    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    return redirect(reverse("users:login"))
