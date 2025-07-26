from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import BlogListView, BlogFilterTopic

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path("", views.CatalogMainView.as_view(), name="main"),
    path("all_products/", views.CatalogListView.as_view(), name="all_products"),
    path("one_product/<int:pk>/", cache_page(60)(views.CatalogDetailView.as_view()), name="one_product"),
    path("all_products_filter/<int:pk>/", views.ProductsFilterCategory.as_view(), name="all_products_filter"),
    path("contacts/", views.CatalogContactsView.as_view(), name="contacts"),
    path("pay/", views.CatalogPayView.as_view(), name="pay"),
    path("sorry/", views.CatalogSorryView.as_view(), name="sorry"),

    path("all_blogs/", BlogListView.as_view(), name="all_blogs"),
    path("all_blogs_filter/<int:pk>/", BlogFilterTopic.as_view(), name="all_blogs_filter"),

    path("create_product/", views.CatalogCreateView.as_view(), name="create_product"),
    path("update_product/<int:pk>/", views.CatalogUpdateView.as_view(), name="update_product"),
    path("delete_product/<int:pk>/", views.CatalogDeleteView.as_view(), name="delete_product"),

]
