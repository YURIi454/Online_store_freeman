from django.db import models



class Category(models.Model):
    """ Модель Category"""

    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(max_length=500, verbose_name='описание')

    def __str__(self):
        """ Вывод информации"""

        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """ Модель Product"""

    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(max_length=1200, verbose_name='описание')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(decimal_places=2, max_digits=14, null=True, verbose_name='цена')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        """ Вывод информации"""

        return f'{self.name} {self.description} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
