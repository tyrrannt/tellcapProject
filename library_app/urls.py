from django.urls import path
from . import views

app_name = 'library_app'

urlpatterns = [
    path('', views.UnitsList.as_view(), name='index'),
    path('add/', views.UnitsAdd.as_view(), name='units_add'),
    path('content/<int:pk>/', views.UnitsDetail.as_view(), name='units_detail'),
    ]
