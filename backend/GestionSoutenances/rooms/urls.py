from django.urls import path
from .views import list, add, update, delete
from .views import RoomsListFilter, RoomsListSearch

urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('filter/', RoomsListFilter.as_view(), name='filter'),
    path('search/', RoomsListSearch.as_view(), name='search'),

]
