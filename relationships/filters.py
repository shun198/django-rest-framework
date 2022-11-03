import django_filters
from relationships.models import (
    Customer,
    Workplace,
)

class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name",lookup_expr="contains")
    workplace = django_filters.CharFilter(field_name="workplace",lookup_expr="contains")

    class Meta:
        model = Customer
        fields = ["name","workplace"]


class WorkPlaceFilter(django_filters.FilterSet):
    customer = django_filters.CharFilter(field_name="customer__name",lookup_expr="contains")
    name = django_filters.CharFilter(field_name="name",lookup_expr="contains")
    created_at = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Workplace
        fields = ["customer","name","created_at"]
