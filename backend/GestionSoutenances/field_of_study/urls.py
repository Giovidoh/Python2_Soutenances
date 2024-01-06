from django.urls import path

from .views import list
from .views import add

urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add')
]
