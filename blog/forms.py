import re

from django import forms
from django.core.exceptions import ValidationError

from blog.models import Blog
from config.settings import ALLOWED_EXTENSIONS, STOP_LIST


class BlogForm(forms.ModelForm):
    """ Форма создания блога. """

    class Meta:
        model = Blog
        fields = ["name", "description", "image", ]

    def __init__(self, *args, **kwargs):

        super(BlogForm, self).__init__(*args, **kwargs)

        self.stop_list = STOP_LIST
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

    def clean_name(self):
        """Проверка на недопустимые имена."""

        name = self.cleaned_data.get("name").strip().lower()

        pattern = r'\b({})\b'.format('|'.join(map(re.escape, map(lambda x: x.lower(), self.stop_list))))

        match = re.search(pattern, name)
        if match:
            raise forms.ValidationError(f'Недопустимое название блога "{match.group()}".')

        return name

    def clean_description(self):
        """ Проверка текста описания на недопустимые слова. """

        description = self.cleaned_data.get("description", "").strip().lower()

        pattern = r'\b({})\b'.format('|'.join(map(re.escape, map(lambda x: x.lower(), self.stop_list))))

        match = re.search(pattern, description)
        if match:
            raise forms.ValidationError(f'В описании присутствует недопустимое слово "{match.group()}".')

        return description

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


class BlogFormAdmin(BlogForm, forms.ModelForm):
    """  Форма блога для администратора. """

    class Meta:
        model = Blog
        fields = BlogForm.Meta.fields + ["publication", "blog_owner", "topic", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["publication"].widget.attrs.update(
            {'class': 'form-select',
             'placeholder': ''}
        )
        self.fields["blog_owner"].widget.attrs.update(
            {'class': 'form-select',
             'placeholder': ''}
        )
        self.fields["topic"].widget.attrs.update(
            {'class': 'form-select',
             'placeholder': ''}
        )


class BlogFormContentMan(forms.ModelForm):
    """  Форма редактирования блога для контент-менеджера. """

    class Meta:
        model = Blog
        fields = ["publication", "topic", ]

    def __init__(self, *args, **kwargs):
        super(BlogFormContentMan, self).__init__(*args, **kwargs)

        self.fields["publication"].widget.attrs.update(
            {'class': 'form-select',
             'placeholder': ''}
        )
        self.fields["topic"].widget.attrs.update(
            {'class': 'form-select',
             'placeholder': ''}
        )
