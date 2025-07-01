from catalog.models import Product

from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy


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


class CatalogContactsView(TemplateView):
    """ Шаблон контактные данные. """

    template_name = 'contacts.html'
    success_url = reverse_lazy('contacts')


class CatalogPayView(TemplateView):
    """ Шаблон формы оплаты. """

    template_name = 'pay.html'
    success_url = reverse_lazy('pay')
