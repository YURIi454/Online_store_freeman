from django.core.management.base import BaseCommand
from blog.models import Topic

class Command(BaseCommand):
    help = 'Создание таблицы Topic с наполнением для работы приложения Blog '

    def handle(self, *args, **options):
        topics = [
            {"name": "auto"},
            {"name": "travel"},
            {"name": "food"},
            {"name": "devices"},
            {"name": "hobby"},
        ]

        for topic_ in topics:
            topic, created = Topic.objects.get_or_create(**topic_)
            if created:
                self.stdout.write(f'Тема "{topic.name}" создана.')
            else:
                self.stdout.write(f'Тема "{topic.name}" уже есть.')

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена темами будущих блогов.'))