from django.db import models


class Blog(models.Model):
    """ Модель Blog"""

    name = models.CharField(max_length=150, verbose_name='заголовок')
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        default='Нет содержимого',
        verbose_name='Содержимое')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateField(auto_now=True, verbose_name='Изменён')
    publication = models.BooleanField(default=False, verbose_name='Опубликовать')
    watch_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        """ Вывод информации"""

        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
