from django.urls import path
from .views import list, add

urlpatterns = [
    path('list/', list, name = 'list'),
    path('add/', add, name = 'add'),
]
