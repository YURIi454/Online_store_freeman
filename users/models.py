from django.db import models
from django.contrib.auth.models import AbstractUser


class  CustomUser(AbstractUser):
    """ Модель пользователя. """

    email = models.EmailField(unique=True, verbose_name="Ваш Email")
    avatar = models.ImageField(upload_to="avatars/",null=True, blank=True,verbose_name="Добавьте аватар")
    phone_num = models.CharField(max_length=15, null=True, blank=True, verbose_name="Ваш номер телефона")
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name="Страна")


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username",]

    def __str__(self):
        return self.email
