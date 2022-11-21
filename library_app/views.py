from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from library_app.forms import UnitsAddForm
from library_app.models import UnitMainModel, UnitChildModel


# Create your views here.

class UnitsList(ListView):
    model = UnitChildModel



class UnitsAdd(CreateView):
    model = UnitChildModel
    form_class = UnitsAddForm
    success_url = reverse_lazy('library_app:index')


class UnitsDetail(DetailView):
    model = UnitChildModel
