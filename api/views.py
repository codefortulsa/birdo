from rest_framework import viewsets, filters

from .serializers import (
    BirdSerializer, PermutationSerializer, PermutationTypeSerializer)

from birds.models import Bird, BirdPermutation, PermutationType


class BirdViewSet(viewsets.ModelViewSet):
    queryset = Bird.objects.order_by('id')
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'parent')
    serializer_class = BirdSerializer

    def filter_queryset(self, queryset):
        qs = super(BirdViewSet, self).filter_queryset(queryset)
        if 'parent' in self.request.QUERY_PARAMS:
            filter_value = self.request.QUERY_PARAMS['parent']
            if not filter_value:
                qs = qs.filter(parent=None)
        return qs


class PermutationViewSet(viewsets.ModelViewSet):
    queryset = BirdPermutation.objects.all()
    serializer_class = PermutationSerializer


class PermutationTypeViewSet(viewsets.ModelViewSet):
    queryset = PermutationType.objects.all()
    serializer_class = PermutationTypeSerializer
