from django.db import models

from users.models import CustomUser


class Category(models.Model):
    """ Модель Category"""

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')

    def __str__(self):
        """ Вывод информации"""

        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """ Модель Product"""

    publication_status = [
        ('moderation', 'На модерации'),
        ('approved', 'Опубликовано'),
        ('need_fix', 'Исправить'),
        ('rejected', 'Отклонено'),
    ]

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(
        max_length=1500,
        null=True,
        blank=True,
        verbose_name='Описание'
    )
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.DecimalField(
        decimal_places=2,
        max_digits=14,
        null=True,
        blank=True,
        default=0.00,
        verbose_name='Цена'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    product_owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Добавил',
        null=True,
        blank=True
    )
    publication = models.CharField(
        max_length=13,
        default='moderation',
        choices=publication_status,
        verbose_name='Статус проверки'
    )

    def __str__(self):
        """ Вывод информации"""

        return f'{self.name} {self.description} {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        permissions = [
            ('redact_status_product', 'Изменение статуса публикации товара'),
        ]
