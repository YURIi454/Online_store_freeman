from django.urls import path

from blog.views import BlogListView

from . import views

app_name = 'catalog'

urlpatterns = [
    path("", views.CatalogMainView.as_view(), name="main"),
    path("all_products/", views.CatalogListView.as_view(), name="all_products"),
    path("one_product/<int:pk>/", views.CatalogDetailView.as_view(), name="one_product"),
    path("contacts/", views.CatalogContactsView.as_view(), name="contacts"),
    path("pay/", views.CatalogPayView.as_view(), name="pay"),
    path("all_blogs/", BlogListView.as_view(), name="all_blogs"),

    path("create_product/", views.CatalogCreateView.as_view(), name="create_product"),
    path("update_product/<int:pk>/", views.CatalogUpdateView.as_view(), name="update_product"),
    path("delete_product/<int:pk>/", views.CatalogDeleteView.as_view(), name="delete_product"),

]
