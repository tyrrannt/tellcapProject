from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import Textarea

from library_app.models import UnitChildModel


class UnitsAddForm(forms.ModelForm):
    # description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = UnitChildModel
        fields = ['title', 'description', 'is_active']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 40}),
        }
