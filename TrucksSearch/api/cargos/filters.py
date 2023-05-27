from django.db.models import Value
from django_filters import rest_framework as filters


class CargoFilter(filters.FilterSet):
    min_weight = filters.NumberFilter(field_name="weight", lookup_expr='gte')
    max_weight = filters.NumberFilter(field_name="weight", lookup_expr='lte')
    miles = filters.NumberFilter(
        method='set_max_distance', label='Max distance'
    )

    def set_max_distance(self, queryset, name, value):
        return queryset.annotate(max_distance=Value(value))
