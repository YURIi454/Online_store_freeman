import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from catalog.models import Product
from config.settings import ALLOWED_EXTENSIONS, STOP_LIST


class ContactForm(forms.Form):
    """ Форма для обратной связи. """

    name = forms.CharField(
        max_length=100,
        required=True,
        validators=[MinLengthValidator(2)],
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше имя'})
    )
    email = forms.EmailField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ваш email'})
    )
    message = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ваше сообщение',
            'rows': 3})
    )


class ProductForm(forms.ModelForm):
    """ Форма создания товара. """

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):

        super(ProductForm, self).__init__(*args, **kwargs)

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
        self.fields["category"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["price"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите цену'}
        )

    def clean_name(self):
        """Проверка на недопустимые имена."""

        name = self.cleaned_data.get("name").strip().lower()

        pattern = r'\b({})\b'.format('|'.join(map(re.escape, map(lambda x: x.lower(), self.stop_list))))

        match = re.search(pattern, name)
        if match:
            raise forms.ValidationError(f'Недопустимое название товара "{match.group()}".')

        return name

    def clean_description(self):
        """ Проверка всего текста описания на запретные слова. """

        description = self.cleaned_data.get("description", "").strip().lower()

        pattern = r'\b({})\b'.format('|'.join(map(re.escape, map(lambda x: x.lower(), self.stop_list))))

        match = re.search(pattern, description)
        if match:
            raise forms.ValidationError(f'В описании присутствует недопустимое слово "{match.group()}".')

        return description

    def clean_price(self):
        """ Проверка цены. """
        price = self.cleaned_data.get("price", "")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

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


class ProductFormAdmin(ProductForm, forms.ModelForm):
    """  Форма создания товара для администратора. """

    class Meta:
        model = Product
        fields = ProductForm.Meta.fields + ["publication", "product_owner"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["publication"].widget.attrs.update(
            {'class': 'form-select',
             'placeholder': ''}
        )
        self.fields["product_owner"].widget.attrs.update(
            {'class': 'form-select',
             'placeholder': ''}
        )


class ProductFormModerator(forms.ModelForm):
    """  Форма редактирования товара для модератора. """

    class Meta:
        model = Product
        fields = ["publication", ]

    def __init__(self, *args, **kwargs):
        super(ProductFormModerator, self).__init__(*args, **kwargs)

        self.fields["publication"].widget.attrs.update(
            {'class': 'form-select',
             'placeholder': ''}
        )
