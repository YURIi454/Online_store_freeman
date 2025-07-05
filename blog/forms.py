from django import forms
from django.core.exceptions import ValidationError

from blog.models import Blog
from config.settings import ALLOWED_EXTENSIONS


class BlogForm(forms.ModelForm):
    """ Форма создания блога. """

    class Meta:
        model = Blog
        fields = ["name", "description", "image", "publication"]

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.allowed_extensions = ALLOWED_EXTENSIONS

        self.fields["name"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите имя'}
        )
        self.fields["description"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите описание',
             'rows': 3}
        )
        self.fields["image"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["publication"].widget.attrs.update(
            {'class': 'form-check-input',
             'placeholder': ''}
        )

    def clean_image(self):
        """ Проверка размера и типа  изображения. """

        image = self.cleaned_data.get('image')
        max_size = 5 * 1024 * 1024

        if image:
            image_name = image.name.lower()
            if not any(image_name.endswith(ext) for ext in self.allowed_extensions):
                raise ValidationError('Допустимые типы файла  .jpeg , .jpg , .png')

            if image.size > max_size:
                raise ValidationError('Размер файла не должен превышать 5 Мб ')
            return image
