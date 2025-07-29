from django import forms
from src.books.models import Book



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'publisher',
            'description',
            'pages',
            'language'
            ]
