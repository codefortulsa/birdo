from rest_framework import serializers

from birds.models import Bird, BirdPermutation, PermutationType
from .fields import MPTTRelationField, StraightJSONField


class PermutationTypeSerializer(serializers.ModelSerializer):

    resource_uri = serializers.HyperlinkedIdentityField(
        view_name='api:permutation-type-detail', read_only=True)

    class Meta:
        model = PermutationType
        fields = ('id', 'resource_uri', 'name')


class PermutationTypeDetailSerializer(PermutationTypeSerializer):

    bird_perms = serializers.HyperlinkedRelatedField(
        many=True, view_name='api:permutation-detail', read_only=True)

    class Meta:
        model = PermutationType
        fields = ('id', 'resource_uri', 'name', 'bird_perms')


class PermutationSerializer(serializers.ModelSerializer):
    types = PermutationTypeSerializer(many=True)

    resource_uri = serializers.HyperlinkedIdentityField(
        view_name='api:permutation-detail', read_only=True)
    bird = serializers.HyperlinkedRelatedField(
        view_name='api:bird-detail', read_only=True)
    details = StraightJSONField()

    class Meta:
        model = BirdPermutation
        fields = ('id', 'resource_uri', 'types', 'bird', 'vispedia_id',
                  'vispedia_url', 'details')


class BirdSerializer(serializers.ModelSerializer):
    children = MPTTRelationField(many=True, read_only=True)
    permutations = PermutationSerializer(many=True)

    resource_uri = serializers.HyperlinkedIdentityField(
        view_name='api:bird-detail', read_only=True)
    details = StraightJSONField()

    class Meta:
        model = Bird
        fields = ('id', 'resource_uri', 'name', 'order', 'vispedia_id',
                  'vispedia_url', 'children', 'parent', 'permutations',
                  'details')
