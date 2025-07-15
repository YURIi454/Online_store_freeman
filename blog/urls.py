from django.urls import path

from blog.views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView

app_name = 'blog'

urlpatterns = [
    path("all_blogs/", BlogListView.as_view(), name="all_blogs"),
    path("one_blog/<int:pk>/", BlogDetailView.as_view(), name="one_blog"),

    path("create_blog/", BlogCreateView.as_view(), name="create_blog"),
    path("update_blog/<int:pk>/", BlogUpdateView.as_view(), name="update_blog"),
    path("confirm_delete/<int:pk>/", BlogDeleteView.as_view(), name="confirm_delete")
]
