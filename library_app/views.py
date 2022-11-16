from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from library_app.forms import UnitsAddForm
from library_app.models import UnitModel


# Create your views here.

class UnitsList(ListView):
    model = UnitModel


class UnitsAdd(CreateView):
    model = UnitModel
    form_class = UnitsAddForm
    success_url = reverse_lazy('library_app:index')
