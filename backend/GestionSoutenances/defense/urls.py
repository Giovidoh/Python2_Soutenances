from django.urls import path

from .views import list, add, addMark, update, delete
from .views import DefensesListFilter, DefensesListSearch


urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add'),
    path('addMark/', addMark, name='addMark'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('filter/', DefensesListFilter.as_view(), name='filter'),
    path('search/', DefensesListSearch.as_view(), name='search'),

]
