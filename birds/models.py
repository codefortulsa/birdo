from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from django_extensions.db.models import TimeStampedModel

from shares.models import Share


class Bird(MPTTModel, TimeStampedModel):
    """
    Birds are heirarchically organized to support sub types and for
    searchability when needing to find all references to a group of birds.
    """
    name = models.CharField(max_length=255, unique=True, db_index=True)
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children', db_index=True)
    order = models.PositiveSmallIntegerField(blank=False, default=0)
    vispedia_id = models.CharField(
        blank=True, null=True, max_length=50, unique=True, db_index=True)

    shares = models.ManyToManyField(
        Share, related_name='birds', blank=True)

    class Meta:
        ordering = ('order', 'created',)

    class MPTTMeta:
        order_insertion_by = ('order',)

    def __unicode__(self):
        return self.name


class PermutationType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class BirdPermutation(models.Model):
    types = models.ManyToManyField(PermutationType, related_name='bird_perms')
    bird = models.ForeignKey(Bird, related_name='permutations')
    vispedia_id = models.CharField(
        blank=True, null=True, max_length=50, unique=True, db_index=True)

    def __unicode__(self):
        # return ", ".join(self.types.all())
        return "temp"



# TODO: grab bird image data from this endpoint.
# http://visipedia-load-balancer-254488388.us-east-1.elb.amazonaws.com/taxons/categories/<vispedia_id>/basic_details/
