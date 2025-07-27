from catalog.models import Product


def get_list_products(category_id):
    """ Список товаров в выбранной категории. """

    return Product.objects.filter(category=category_id)
