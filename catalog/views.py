from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import DetailView, FormView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ContactForm, ProductForm
from catalog.models import Product


class CatalogMainView(TemplateView):
    """ Шаблон главной страницы. """

    template_name = 'main.html'
    success_url = reverse_lazy('main')


class CatalogListView(ListView):
    """ Шаблон каталога товаров."""

    model = Product
    template_name = 'catalog/all_products.html'
    success_url = reverse_lazy('catalog:product_list')


class CatalogDetailView(DetailView):
    """ Шаблон подробной информации о продукте. """

    model = Product
    template_name = 'one_product.html'
    context_object_name = 'product'


class CatalogContactsView(FormView):
    """ Шаблон контактные данные. """

    form_class = ContactForm
    template_name = 'contacts.html'
    success_url = reverse_lazy('catalog:main')

    def post(self, request, *args, **kwargs):
        """ Вывод шаблона "спасибо" после отправки формы. """

        response = render(request, "thank_you.html", {})
        response["Refresh"] = "3; url=/"
        return response


class CatalogPayView(TemplateView):
    """ Шаблон формы оплаты. """

    template_name = 'pay.html'
    success_url = reverse_lazy('pay')

class CatalogSorryView(TemplateView):
    """ Шаблон страницы в разработке. """

    template_name = 'sorry.html'
    success_url = reverse_lazy('sorry')


class CatalogCreateView(CreateView):
    """ Добавление нового продукта."""

    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'

    def get_success_url(self):
        """ Перенаправление на страницу созданного продукта. """

        return reverse_lazy("catalog:one_product", kwargs={"pk": self.object.pk})


class CatalogUpdateView(UpdateView):
    """ Редактирование выбранного  продукта."""

    model = Product
    form_class = ProductForm

    template_name = 'update_product.html'

    def get_success_url(self):
        """ Перенаправление на страницу созданного продукта. """

        return reverse_lazy("catalog:one_product", kwargs={"pk": self.object.pk})


class CatalogDeleteView(DeleteView):
    """ Удаление выбранного продукта. """

    model = Product

    template_name = "confirm_delete_product.html"
    success_url = reverse_lazy('catalog:all_products')
