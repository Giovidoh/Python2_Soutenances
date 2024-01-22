from django.urls import path

from .views import list, add, addMark, update, delete

urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add'),
    path('addMark/', addMark, name='addMark'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]
