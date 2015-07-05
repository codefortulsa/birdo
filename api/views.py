from rest_framework import viewsets, filters
from rest_framework_extensions.mixins import DetailSerializerMixin
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import (
    BirdSerializer, PermutationSerializer, PermutationTypeSerializer,
    PermutationTypeDetailSerializer)

from birds.models import Bird, BirdPermutation, PermutationType

from .filters import BirdFilter


class BirdViewSet(
        CacheResponseMixin,
        viewsets.ModelViewSet):
    """
    Search for birds and bird categories.

    Use the `object_type` query param to limit results to bird categories and
    individual birds. `leafs` for birds, and `branches` for categories.
    """

    queryset = Bird.objects.order_by('id')
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BirdFilter
    serializer_class = BirdSerializer

    def filter_queryset(self, queryset):
        qs = super(BirdViewSet, self).filter_queryset(queryset)
        if 'parent' in self.request.QUERY_PARAMS:
            filter_value = self.request.QUERY_PARAMS['parent']
            if not filter_value:
                qs = qs.filter(parent=None)
        return qs


class PermutationViewSet(
        CacheResponseMixin,
        viewsets.ModelViewSet):
    queryset = BirdPermutation.objects.all()
    serializer_class = PermutationSerializer


class PermutationTypeViewSet(
        CacheResponseMixin,
        DetailSerializerMixin,
        viewsets.ModelViewSet):
    queryset = PermutationType.objects.all()
    serializer_class = PermutationTypeSerializer
    serializer_detail_class = PermutationTypeDetailSerializer
