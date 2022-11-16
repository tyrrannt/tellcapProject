from django import forms

from library_app.models import UnitModel


class UnitsAddForm(forms.ModelForm):
    class Meta:
        model = UnitModel
        fields = ['parent_category', 'title', ]
