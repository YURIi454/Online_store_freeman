from django.db import models

from users.models import CustomUser


class Topic(models.Model):
    """ Модель темы блога. """

    topic_list = [
        ("auto", "авто / мото"),
        ("travel", "путешествия"),
        ("food", "еда"),
        ("devices", "гаджеты"),
        ("hobby", "хобби / отдых / спорт"),
    ]

    name = models.CharField(choices=topic_list, null=True, blank=True, default="auto", max_length=22,
                            verbose_name='Тема блога')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        """ Вывод информации"""

        return f'{self.name}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


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
    topic = models.ForeignKey(
        Topic,
        on_delete=models.PROTECT,
        related_name='blogs',
        verbose_name='Тема блога', null=True,
        blank=True, )
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

        return f'{self.name} {self.topic}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        permissions = [
            ('change_status_blog', 'Изменение статуса публикации блога'),
            ('change_topic_blog', 'Изменение темы блога'),
        ]
