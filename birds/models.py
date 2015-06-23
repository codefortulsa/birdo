from django.db import models
from django_pgjson.fields import JsonField
from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from django_extensions.db.models import TimeStampedModel

from shares.models import Share


class VispediaURLMixin(object):

    @property
    def vispedia_url(self):
        return (
            "http://visipedia-load-balancer-254488388.us-east-1.elb."
            "amazonaws.com/taxons/categories/{}/basic_details/"
            "?format=json").format(self.vispedia_id)


class BirdQuerySet(models.QuerySet):

    def leafs(self):
        "Leaf birds do not contain anything"
        return self.filter(lft=models.F('rght') - 1)

    def branches(self):
        "Branches contain children"
        return self.exclude(lft=models.F('rght') - 1)


class BirdManager(TreeManager):

    def get_queryset(self):
        return BirdQuerySet(self.model, using=self._db)

    def leafs(self):
        return self.get_queryset().leafs()

    def branches(self):
        return self.get_queryset().branches()


class Bird(VispediaURLMixin, MPTTModel, TimeStampedModel):

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
    details = JsonField(null=True, blank=True)

    shares = models.ManyToManyField(
        Share, related_name='birds', blank=True)

    objects = BirdManager()

    class Meta:
        ordering = ('order', 'created',)

    class MPTTMeta:
        order_insertion_by = ('order',)

    def __unicode__(self):
        return self.name

    @property
    def ancestors(self):
        return self.get_ancestors(include_self=True)


class PermutationType(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class BirdPermutation(VispediaURLMixin, models.Model):
    types = models.ManyToManyField(PermutationType, related_name='bird_perms')
    bird = models.ForeignKey(Bird, related_name='permutations')
    vispedia_id = models.CharField(
        blank=True, null=True, max_length=50, unique=True, db_index=True)

    def __unicode__(self):
        return "{} [{}]".format(
            self.bird, ', '.join(map(lambda tag: str(tag), self.types.all())))
