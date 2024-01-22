from django.urls import path
from .views import list, add, update, delete, deletedProfList
from .views import ProfessorsListFilter, ProfessorsListSearch


urlpatterns = [
    path('list/', list, name='list'),
    path('add/', add, name='add'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('deletedProfList/', deletedProfList, name='deletedProf'),
    path('filter/', ProfessorsListFilter.as_view(), name='filter'),
    path('search/', ProfessorsListSearch.as_view(), name='search'),

]
