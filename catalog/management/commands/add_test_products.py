from django.core.management import BaseCommand, call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    """ Класс кастомных команд добавления продуктов в базу данных."""

    help = 'Загрузка данных из фикстуры'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Данные успешно добвалены!'))
