from django.db import models


class Blog(models.Model):
    """ Модель Blog"""

    name = models.CharField(max_length=150, verbose_name='заголовок')
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        default='нет содержимого.',
        verbose_name='содержимое')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='изображение')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    publication = models.BooleanField(default=False)
    watch_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        """ Вывод информации"""

        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
