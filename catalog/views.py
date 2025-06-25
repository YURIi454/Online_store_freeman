from django.shortcuts import render

from catalog.models import Product


def catalog_base(request):
    """ Загрузка базового шаблона."""

    return render(request, "catalog/base.html")


def catalog_contacts(request):
    """ Загрузка шаблона с контактными данными. """

    return render(request, "catalog/contacts.html")


def catalog_pay(request):
    """ Загрузка подшаблона формы оплаты. """

    return render(request, "catalog/pay.html")


def catalog_all_product(request):
    """ Загрузка подшаблона всех продуктов. """

    product = Product.objects.all()
    context = {
        "product": product
    }
    return render(request, "catalog/all_products.html", context=context)


def catalog_one_product(request,product_id):
    """ Загрузка подшаблона формы оплаты. """

    product = Product.objects.get(id=product_id)
    context = {
        "product": product
    }
    return render(request, "catalog/one_product.html", context=context)
