from django.urls import path

from .views import list, add, update, delete
from .views import FieldsListFilter, FieldsListSearch

urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('filter/', FieldsListFilter.as_view(), name='filter'),
    path('search/', FieldsListSearch.as_view(), name='search'),

]
