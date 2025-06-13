""" Конфигурация URL для проекта config.

Список urlpatterns сопоставляет URL-адреса с представлениями.
Дополнительную информацию см.: https://docs.djangoproject.com/en/5.2/topics/http/urls
Примеры: Представления-функции
1. Добавьте импорт: от моего_приложения импортируйте представления
2. Добавьте URL в список urlpatterns: path('', views.home, name='home')
Представления на основе классов
1. Добавьте импорт: от представлений другого_приложения импортируйте Home
2. Добавьте URL в список urlpatterns: path('', Home.as_view(), name='home')
Подключение другой конфигурации URL
1. Импортируйте функцию include(): от django.urls импортируйте include, path
2. Добавьте URL в список urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("catalog.urls")),
]
