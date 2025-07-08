from django.db import models


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

    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(
        max_length=1200,
        null=True,
        blank=True,
        verbose_name='Описание')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.DecimalField(
        decimal_places=2,
        max_digits=14,
        null=True,
        blank=True,
        default=0.00,
        verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        """ Вывод информации"""

        return f'{self.name} {self.description} {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
