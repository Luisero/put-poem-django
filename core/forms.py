from django import forms
from .models import Poem
from ckeditor.widgets import CKEditorWidget


class PoemForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Poem 
        fields = ['title', 'content',]