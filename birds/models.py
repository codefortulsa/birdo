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

    class Meta:
        ordering = ('order', 'created',)

    class MPTTMeta:
        order_insertion_by = ('order',)

    def __unicode__(self):
        return self.name


class SharedBird(Bird):
    shares = models.ManyToManyField(Share, related_name='birds')
