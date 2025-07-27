from django.core.management.base import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    help = 'Создание таблицы Category с наполнением для работы приложения Catalog '

    def handle(self, *args, **options):
        categories = [
            {"name": "auto"},
            {"name": "travel"},
            {"name": "food"},
            {"name": "devices"},
            {"name": "hobby"},
        ]

        for category in categories:
            category, created = Category.objects.get_or_create(**category)
            if created:
                self.stdout.write(f'Категория "{category.name}" создана.')
            else:
                self.stdout.write(f'Категория "{category.name}" уже есть.')

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена категориями будущих товаров.'))
