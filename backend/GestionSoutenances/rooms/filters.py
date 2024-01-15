import django_filters
from .models import Rooms

class RoomsFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search')

    class Meta:
        model = Rooms
        fields = ['search']

    def filter_search(self, queryset, name, value):
        return queryset.search(value)
