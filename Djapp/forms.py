from django.forms import ModelForm, ClearableFileInput

from Djapp.models import Books


class book_form(ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'author', 'file')
