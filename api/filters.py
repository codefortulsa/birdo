import django_filters

from birds.models import Bird


class BirdFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='icontains')
    object_type = django_filters.MethodFilter(action='get_object_type')

    class Meta:
        model = Bird
        fields = ('name', 'parent', 'vispedia_id', 'object_type')

    def get_object_type(self, qs, value):
        if value in ['leafs', 'branches']:
            return getattr(qs, value)()
        return qs
