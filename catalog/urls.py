from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path("", views.CatalogMainView.as_view(), name="main"),
    path("all_products/", views.CatalogListView.as_view(), name="all_products"),
    path("one_product/<int:pk>/", views.CatalogDetailView.as_view(), name="one_product"),
    path("contacts/", views.CatalogContactsView.as_view(), name="contacts"),
    path("pay/", views.CatalogPayView.as_view(), name="pay"),
    path("blog/", views.CatalogBlogView.as_view(), name="blog"),
]
