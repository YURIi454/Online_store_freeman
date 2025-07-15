from django.db import models

from users.models import CustomUser


class Blog(models.Model):
    """ Модель Blog"""

    publication_status = [
        ('moderation', 'На модерации'),
        ('approved', 'Опубликовано'),
        ('need_fix', 'Исправить'),
        ('rejected', 'Отклонено'),
    ]

    name = models.CharField(max_length=150, verbose_name='Название блога')
    description = models.TextField(
        max_length=3000,
        null=True,
        blank=True,
        default='Пока нет описания',
        verbose_name='Описание'
    )
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateField(auto_now=True, verbose_name='Изменён')
    publication = models.CharField(
        max_length=20,
        choices=publication_status,
        default='moderation',
        verbose_name='Статус проверки'
    )
    watch_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')
    blog_owner = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='blogs',
        verbose_name='Создал',
        null=True,
        blank=True
    )

    def __str__(self):
        """ Вывод информации"""

        return f'{self.name}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        permissions = [
            ('redact_status_blog', 'Изменение статуса публикации блога'),
        ]
