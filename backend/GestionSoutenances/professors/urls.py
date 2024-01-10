from django.urls import path
from .views import list, add, update, delete, search, deletedProfList

urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('search/<str:name>/<str:firstName>', search, name='search'),
    path('deletedProfList/', deletedProfList, name='deletedProf'),
]
