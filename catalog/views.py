from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ContactForm, ProductForm, ProductFormAdmin, ProductFormModerator
from catalog.models import Product


class CatalogMainView(TemplateView):
    """ Шаблон главной страницы. """

    template_name = 'main.html'
    success_url = reverse_lazy('main')


class CatalogPayView(TemplateView):
    """ Шаблон формы оплаты. """

    template_name = 'pay.html'
    success_url = reverse_lazy('pay')


class CatalogSorryView(TemplateView):
    """ Шаблон страницы в разработке. """

    template_name = 'sorry.html'
    success_url = reverse_lazy('sorry')


class CatalogContactsView(FormView):
    """ Шаблон страницы с контактными данными. """

    form_class = ContactForm
    template_name = 'contacts.html'
    success_url = reverse_lazy('catalog:main')

    def post(self, request, *args, **kwargs):
        """ Вывод шаблона "спасибо" после отправки формы. """

        response = render(request, "thank_you.html", {})
        response["Refresh"] = "3; url=/"
        return response


class CatalogListView(ListView):
    """ Список товаров с фильтрацией по группам."""

    model = Product
    template_name = 'catalog/all_products.html'

    def get_queryset(self):
        """ Фильтр отображения модели. """

        if self.request.user.is_superuser or self.request.user.groups.filter(name='Administrators').exists():
            return Product.objects.all()
        if (self.request.user.groups.filter(name='Moderators').exists() or
                self.request.user.groups.filter(name='Content-managers').exists()):
            return Product.objects.all()
        if self.request.user.is_authenticated:
            return Product.objects.filter(Q(product_owner=self.request.user) | Q(publication='approved'))
        else:
            return Product.objects.filter(publication='approved')


class CatalogDetailView(DetailView):
    """ Подробная информации о товаре. """

    model = Product
    template_name = 'one_product.html'
    context_object_name = 'product'


class CatalogCreateView(LoginRequiredMixin, CreateView):
    """ Добавление нового продукта. """

    model = Product
    template_name = 'create_product.html'

    def get_form_class(self):
        """ Выбор нужной формы для администратора или модератора. """

        if self.request.user.is_superuser or self.request.user.groups.filter(name='Administrators').exists():
            return ProductFormAdmin
        elif (self.request.user.groups.filter(name='Moderators').exists() or
              self.request.user.groups.filter(name='Content-managers').exists()):
            raise PermissionDenied(" Извините у вас недостаточно прав.")

        else:
            return ProductForm

    def form_valid(self, form):
        """ Заполнение поля product_owner данными текущего пользователя. """

        form.instance.product_owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """ Перенаправление на страницу созданного продукта. """

        return reverse_lazy("catalog:one_product", kwargs={"pk": self.object.pk})


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    """ Редактирование выбранного продукта."""

    model = Product
    template_name = 'update_product.html'

    def get_form_class(self):
        """ Выбор нужной формы для пользователя, администратора или модератора. """

        if self.request.user.is_superuser or self.request.user.groups.filter(name='Administrators').exists():
            return ProductFormAdmin
        if self.request.user.groups.filter(name='Moderators').exists():
            return ProductFormModerator
        if self.request.user.is_authenticated and self.get_object().product_owner == self.request.user:
            return ProductForm
        else:
            raise PermissionDenied(" Извините у вас недостаточно прав.")

    def get_success_url(self):
        """ Перенаправление на страницу отредактированного продукта. """

        return reverse_lazy("catalog:one_product", kwargs={"pk": self.object.pk})


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    """ Удаление выбранного продукта. """

    model = Product
    success_url = reverse_lazy('catalog:all_products')

    def get_template_names(self):
        """ Проверка прав доступа на удаление товара. """

        user = self.request.user
        if (user == self.object.product_owner or
                user.groups.filter(name="Moderators").exists() or
                user.groups.filter(name="Administrators").exists()):
            return ["confirm_delete_product.html", ]
        raise PermissionDenied(" Извините у вас недостаточно прав.")
