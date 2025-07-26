from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.cache import cache

from blog.forms import BlogForm, BlogFormContentMan, BlogFormAdmin
from blog.models import Blog, Topic
from blog.services import get_list_blogs


class BlogListView(ListView):
    """ Список блогов с фильтрацией по группам."""

    model = Blog
    template_name = "blog/all_blogs.html"

    def get_queryset(self):
        """ Фильтр отображения модели. """

        if self.request.user.is_superuser or self.request.user.groups.filter(name='Administrators').exists():
            return Blog.objects.all()
        if (self.request.user.groups.filter(name='Content-managers').exists() or
                self.request.user.groups.filter(name='Moderators').exists()):
            return Blog.objects.all()
        if self.request.user.is_authenticated:
            return Blog.objects.filter(Q(blog_owner=self.request.user) | Q(publication='approved'))
        else:
            return Blog.objects.filter(publication='approved')


class BlogFilterTopic(ListView):
    """ Список блогов с фильтрацией по теме. """

    model = Topic
    template_name = 'all_blogs_filter.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic_id = self.kwargs.get('pk')
        current_topic = Topic.objects.get(pk=topic_id)
        context["topics"] = get_list_blogs(topic_id)
        context["current_topic"] = current_topic
        return context

    def get_queryset(self):
        queryset = cache.get('list_blogs')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('list_blogs', queryset, 60 * 15)
        return queryset


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


class BlogCreateView(LoginRequiredMixin, CreateView):
    """ Создание нового блога. """

    model = Blog
    template_name = "blog/create_blog.html"

    def get_form_class(self):
        """ Выбор нужной формы для администратора или модератора. """

        if self.request.user.is_superuser or self.request.user.groups.filter(name='Administrators').exists():
            return BlogFormAdmin
        elif (self.request.user.groups.filter(name='Moderators').exists() or
              self.request.user.groups.filter(name='Content-managers').exists()):
            raise PermissionDenied(" Извините у вас недостаточно прав.")

        else:
            return BlogForm

    def form_valid(self, form):
        """ Заполнение поля blog_owner данными текущего пользователя. """

        form.instance.blog_owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """ Перенаправление на страницу созданного блога. """

        return reverse("blog:one_blog", kwargs={"pk": self.object.pk})


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """ Редактирование блога. """

    model = Blog
    template_name = "update_blog.html"

    def get_form_class(self):
        """ Выбор нужной формы для пользователя, администратора или модератора. """

        if self.request.user.is_superuser or self.request.user.groups.filter(name='Administrators').exists():
            return BlogFormAdmin
        if self.request.user.groups.filter(name='Content-managers').exists():
            return BlogFormContentMan
        if self.request.user.is_authenticated and self.get_object().blog_owner == self.request.user:
            return BlogForm
        else:
            raise PermissionDenied(" Извините у вас недостаточно прав.")

    def get_success_url(self):
        """ Перенаправление на страницу отредактированного блога. """

        return reverse("blog:one_blog", kwargs={"pk": self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """ Удаление выбранного блога. """

    model = Blog
    success_url = reverse_lazy('blog:all_blogs')

    def get_template_names(self):
        """ Проверка прав доступа на удаление блога. """

        user = self.request.user
        if (user == self.object.blog_owner or
                user.groups.filter(name="Content-managers").exists() or
                user.groups.filter(name="Administrators").exists()):
            return ["confirm_delete.html", ]
        raise PermissionDenied(" Извините у вас недостаточно прав.")
