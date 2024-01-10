from django.urls import path
from .views import list, add, update, delete

urlpatterns = [
    path('list/', list, name = 'list'),
    path('add/', add, name = 'add'),
    path('update/<int:id>/', update, name = 'update'),
    path('delete/<int:id>/', delete, name = 'delete'),
]
