from rest_framework import serializers

from birds.models import Bird, BirdPermutation, PermutationType
from .fields import MPTTRelationField


class GetVispediaURLMixin(object):

    def get_vispedia_url(self, obj):
        return "http://visipedia-load-balancer-254488388.us-east-1.elb.amazonaws.com/taxons/categories/{}/basic_details/?format=json".format(obj.vispedia_id)


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



class PermutationSerializer(GetVispediaURLMixin, serializers.ModelSerializer):
    types = PermutationTypeSerializer(many=True)

    resource_uri = serializers.HyperlinkedIdentityField(
        view_name='api:permutation-detail', read_only=True)
    bird = serializers.HyperlinkedRelatedField(
        view_name='api:bird-detail', read_only=True)

    vispedia_url = serializers.SerializerMethodField()

    class Meta:
        model = BirdPermutation
        fields = ('id', 'resource_uri', 'types', 'bird', 'vispedia_id',
                  'vispedia_url')


class BirdSerializer(GetVispediaURLMixin, serializers.ModelSerializer):
    children = MPTTRelationField(many=True, read_only=True)
    permutations = PermutationSerializer(many=True)

    resource_uri = serializers.HyperlinkedIdentityField(
        view_name='api:bird-detail', read_only=True)

    vispedia_url = serializers.SerializerMethodField()

    class Meta:
        model = Bird
        fields = ('id', 'resource_uri', 'name', 'order', 'vispedia_id',
                  'vispedia_url', 'children', 'parent', 'permutations')
