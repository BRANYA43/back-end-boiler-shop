from functools import reduce

from django.db.models import Count, Q
from django_filters import rest_framework as filters

from products.models import Product
from utils.models import Attribute


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    names = CharFilterInFilter(method='filter_names', label='Name/s is in:')
    category = filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    attributes = CharFilterInFilter(method='filter_attributes', label='Attribute/s is in:')
    price = filters.NumericRangeFilter(method='filter_price', label='Price range from min to max:')

    class Meta:
        model = Product
        fields = ['names', 'category', 'attributes', 'price']

    def filter_names(self, queryset, _, names):
        names_query = [Q(name__icontains=name) for name in names]
        names_query = reduce(lambda q1, q2: q1 | q2, names_query)
        return queryset.filter(names_query)

    def filter_attributes(self, queryset, _, attributes):
        names = []
        values = []
        for attr in attributes:
            name, value = attr.split(':')
            names.append(name)
            values.append(value)
        attr_qs = Attribute.objects.filter(name__in=names, value__in=values)
        return (
            queryset.filter(specification__all_attributes__uuid__in=attr_qs.values('uuid'))
            .annotate(num_products=Count('uuid'))
            .filter(num_products=attr_qs.count())
        )

    def filter_price(self, queryset, _, price_range):
        min_price, max_price = price_range.start, price_range.stop
        return queryset.filter(price__range=(min_price, max_price))
