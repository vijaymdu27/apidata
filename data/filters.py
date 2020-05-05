from .models import ApiView
import django_filters


class ApiViewFilters(django_filters.FilterSet):

    class Meta:
        model = ApiView
        fields = ['title', 'location']
