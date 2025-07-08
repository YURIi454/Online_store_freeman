from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegisterUserView, email_verification, UpdateUserView

app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('update/', UpdateUserView.as_view(), name='update'),
    path('email-confirm/<str:token>/',email_verification, name="email-confirm"),
]
