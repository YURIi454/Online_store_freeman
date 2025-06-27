from catalog.models import Product

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy


class CatalogMainView(TemplateView):
    """ Шаблон главной страницы. """

    template_name = 'catalog/main.html'
    success_url = reverse_lazy('main')

class CatalogListView(ListView):
    """ Шаблон каталога товаров."""

    model = Product
    template_name = 'catalog/all_products.html'
    success_url = reverse_lazy('catalog:product_list')


class CatalogDetailView(DetailView):
    """ Шаблон подробной информации о продукте. """

    model = Product
    template_name = 'catalog/one_product.html'
    context_object_name = 'product'


class CatalogContactsView(TemplateView):
    """ Шаблон контактные данные. """

    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('contacts')


class CatalogPayView(TemplateView):
    """ Шаблон формы оплаты. """

    template_name = 'catalog/pay.html'
    success_url = reverse_lazy('pay')

class CatalogBlogView(TemplateView):
    """ Шаблон формы оплаты. """

    template_name = 'catalog/blog.html'
    success_url = reverse_lazy('blog')

#
# class MyModelCreateView(CreateView):
#     """ Класс создания моделей."""
#
#     model = MyModel
#     fields = ['name', 'description']
#     template_name = 'catalog/test_model.html'
#     success_url = reverse_lazy('catalog:mymodel_list')
#
#
# class MyModelListView(ListView):
#     """ Класс отображения моделей."""
#
#     model = MyModel
#     template_name = 'catalog/test_model_list.html'
#     context_object_name = "mymodels"
#
#     def get_queryset(self):
#         """ Изменение набора данных модели. """
#
#         return MyModel.objects.filter(is_active=True)
#
#
# class MyModelDetailView(DetailView):
#     """ Класс отображения детальной информации. """
#
#     model = MyModel
#     template_name = 'catalog/test_model_detail.html'
#     context_object_name = 'mymodel'
#
#     def get_context_data(self, **kwargs):
#         """ Дополнительные данные для шаблона"""
#
#         context = super().get_context_data(**kwargs)
#         context["More_info"] = "Дополнительная информация."
#
#         return context
#
#
# class MyModelUpdateView(UpdateView):
#     """ Класс обновления информации. """
#
#     model = MyModel
#     fields = ['name', 'description']
#     template_name = 'catalog/test_model.html'
#     success_url = reverse_lazy('catalog:mymodel_list')
#
#
# class MyModelDeleteView(DeleteView):
#     """ Класс удаления информации. """
#
#     model = MyModel
#     template_name = 'catalog/test_model_delete.html'
#     success_url = reverse_lazy('catalog:mymodel_list')
