from django import forms
from django.forms import ModelForm

from .models import Project, Review


class ProjectForm( ModelForm ):
    class Meta:
        model = Project
        fields = ['title', 'slug', 'image', 'tags', 'description', 'demo_link', 'source_link']
        labels = {
            'title': 'Название товара',
            'slug': 'Слаг',
            'image': 'Фото товара',
            'tags': 'Теги',
            'description': 'Описание товара',
            'demo_link': 'Ссылка на промо-акции',
            'source_link': 'Ссылка на сайт компании'
        }

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super( ProjectForm, self ).__init__( *args, **kwargs )

        for name, field in self.fields.items():
            field.widget.attrs.update( {'class': 'input'} )


class ReviewForm( ModelForm ):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Поставьте оценку товару',
            'body': 'Добавьте отзыв о товаре'
        }

    def __init__(self, *args, **kwargs):
        super( ReviewForm, self ).__init__( *args, **kwargs )

        for name, field in self.fields.items():
            field.widget.attrs.update( {'class': 'input'} )
