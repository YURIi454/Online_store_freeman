from django.urls import reverse_lazy, reverse

from blog.models import Blog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogCreateView(CreateView):
    """ Создание нового блога. """

    model = Blog
    fields = ["name", "description", "image", "publication"]
    template_name = "blog/create_blog.html"
    success_url = reverse_lazy('blog:all_blogs')


class BlogListView(ListView):
    """ Список блогов."""

    model = Blog
    template_name = "blog/all_blogs.html"

    def get_queryset(self):
        """ Изменение набора данных модели. """

        return Blog.objects.filter(publication=True)


class BlogDetailView(DetailView):
    """ Подробная информация о блоге."""

    model = Blog
    template_name = "blog/one_blog.html"

    def get_object(self, queryset=None):
        """  Увеличение счётчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.watch_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """ Обновление информации в выбранном блоге. """

    model = Blog
    fields = ["name", "description", "image", "publication"]
    template_name = "update_blog.html"

    def get_success_url(self):
        """ Перенаправление на страницу созданного блога. """

        return reverse("blog:one_blog", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    """ Удаление выбранного блога. """

    model = Blog
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('blog:all_blogs')
