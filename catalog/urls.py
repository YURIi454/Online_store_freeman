from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path("", views.catalog_all_product, name="all_products"),
    path("contacts/", views.catalog_contacts, name="contacts"),
    path("one_product/<int:product_id>/", views.catalog_one_product, name="one_product"),
    path("pay/", views.catalog_pay, name="pay"),
]
