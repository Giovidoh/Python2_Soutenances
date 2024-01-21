from django.urls import path
from .views import list, add, update, delete, filter, search
from .views import RoomsList, RoomsListSearch

urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('filter/', RoomsList.as_view(), name='filter'),
    path('search/', RoomsListSearch.as_view(), name='search'),

]
