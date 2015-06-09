from rest_framework import serializers

from birds.models import Bird, BirdPermutation, PermutationType
from .fields import MPTTRelationField


class PermutationTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PermutationType
        fields = ('id', 'name')


class PermutationSerializer(serializers.ModelSerializer):
    types = PermutationTypeSerializer(many=True)

    class Meta:
        model = BirdPermutation
        fields = ('id', 'types', 'bird', 'vispedia_id')


class BirdSerializer(serializers.ModelSerializer):
    children = MPTTRelationField(many=True, read_only=True)
    permutations = PermutationSerializer(many=True)

    class Meta:
        model = Bird
        fields = ('id', 'name', 'order', 'vispedia_id', 'children',
                  'parent', 'permutations',)
