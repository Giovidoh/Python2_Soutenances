from django.urls import path

from .views import list, add, update

urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add'),
    path('update/<int:id>', update, name='update'),
]
