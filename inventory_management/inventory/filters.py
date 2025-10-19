import django_filters
from .models import InventoryItem

class InventoryItemFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    low_stock = django_filters.BooleanFilter(method='filter_low_stock')

    class Meta:
        model = InventoryItem
        fields = ['category', 'min_price', 'max_price', 'low_stock']

    def filter_low_stock(self, queryset, name, value):
        if value:
            threshold = self.request.query_params.get('threshold', 5)
            try:
                threshold = int(threshold)
            except:
                threshold = 5
            return queryset.filter(quantity__lt=threshold)
        return queryset
