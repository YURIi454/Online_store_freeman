from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.views.generic.edit import UpdateView

from users.models import CustomUser
from django import forms
from config.settings import ALLOWED_EXTENSIONS, STOP_LIST


class CustomUserCreationForm(UserCreationForm):
    """ Форма создания нового пользователя. """

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'avatar', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.allowed_extensions = ALLOWED_EXTENSIONS

        self.fields["email"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["username"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )

        self.fields["avatar"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["password1"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["password2"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )

    def clean_phone_number(self):
        """ Проверка верно введённого номера. """

        phone_num = self.cleaned_data.get('phone_num')
        if phone_num and not phone_num.isdigit():
            raise forms.ValidationError('Только цифры.')
        return phone_num

    def clean_image(self):
        """ Проверка размера и типа  изображения. """

        image = self.cleaned_data.get('avatar')
        max_size = 5 * 1024 * 1024

        if image:
            image_name = image.name.lower()
            if not any(image_name.endswith(ext) for ext in self.allowed_extensions):
                raise ValidationError('Допустимые типы файла  .jpeg , .jpg , .png')

            if image.size > max_size:
                raise ValidationError('Размер файла не должен превышать 5 Мб ')
            return image


class CustomUserUpdateForm(UserChangeForm):
    """ Редактирование профиля пользователя. """

    password = None

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "phone_num",
            "country",
        )

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        self.allowed_extensions = ALLOWED_EXTENSIONS

        self.fields["username"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["email"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )

        self.fields["first_name"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["last_name"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["avatar"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["phone_num"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["country"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )

    def clean_phone_number(self):
        """ Проверка верно введённого номера. """

        phone_num = self.cleaned_data.get('phone_num')
        if phone_num and not phone_num.isdigit():
            raise forms.ValidationError('Только цифры.')
        return phone_num

    def clean_image(self):
        """ Проверка размера и типа  изображения. """

        image = self.cleaned_data.get('avatar')
        max_size = 3 * 1024 * 1024

        if image:
            image_name = image.name.lower()
            if not any(image_name.endswith(ext) for ext in self.allowed_extensions):
                raise ValidationError('Допустимые типы файла  .jpeg , .jpg , .png')

            if image.size > max_size:
                raise ValidationError('Размер файла не должен превышать 5 Мб ')
            return image
