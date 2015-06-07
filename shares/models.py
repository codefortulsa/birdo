from django.contrib.gis.db import models

from django_extensions.db.models import TimeStampedModel


class Tag(TimeStampedModel):
    """
    Tags used on within shares.

    can access search tags via .searchtag property
    """

    name = models.CharField('Tag Name', max_length=50)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.name


class SearchTag(Tag):
    enabled = models.BooleanField(default=True)
    lastrun = models.DateTimeField()


class Share(TimeStampedModel):
    """
    A share represents any post/tweet/snap/poke/prod
    made publicly available on a social network.
    """
    # TODO, network specific ID

    UNKNOWN = 0
    TWITTER = 1
    FACEBOOK = 2
    INSTAGRAM = 3

    NETWORK_CHOICES = (
        (UNKNOWN, 'Unknown'),
        (TWITTER, 'Twitter'),
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram')
    )
    user = models.CharField(
        'User',
        max_length=50,
        help_text='the username of the sharer',
        blank=False)
    network = models.SmallIntegerField(
        'Social Network',
        choices=NETWORK_CHOICES,
        help_text='the network the share occurred',
        blank=False)
    text = models.TextField()
    rel = models.FloatField(
        'Relevance',
        default=0.0,
        help_text='how relevant the share is to birds')
    rel_lastrun = models.DateTimeField(
        'Relevance last run')
    location = models.PointField(blank=True, null=True)
    tags = models.ManyToManyField(
        Tag,
        related_name='shares')

    objects = models.GeoManager()

    def __unicode__(self):
        return "{} @{} - {} [{}]".format(
            self.network, self.user, self.created, ', '.join(self.tags))
