from datetime import datetime

from django.conf import settings
from django.contrib.gis.geos import Point

# import arrow
from twython import Twython

from .base import Network, BirdKeywordMixin
from shares.models import Share


class TwitterNetwork(BirdKeywordMixin, Network):

    # Temporary single tag lookup
    tag = 'Goose'
    network_type = Share.TWITTER

    def init_api(self):
        return Twython(
            settings.TWITTER_KEY,
            settings.TWITTER_SECRET,
            settings.TWITTER_TOKEN,
            settings.TWITTER_TOKEN_SECRET)

    def search_social_shares(self, search_query=''):
        """
        How to search for twitter and return a list
        Only search in a radius surounding america
        """

        self.api.verify_credentials()
        results = self.api.search(
            q=search_query,
            result_type='recent',
            geocode='39,-96,1400mi',
            count='100')
        self.meta = results['search_metadata']
        print('rate limit: {}, resets: {}'.format(
            self.api.get_lastfunction_header('x-rate-limit-remaining'),
            self.api.get_lastfunction_header('x-rate-limit-reset')))
        return results['statuses']

    def calculate_relevance(self, share_model, share_data):
        # if we have a lot of hashtags, don't consider it relevant
        rel = super(TwitterNetwork, self).calculate_relevance(
            share_model, share_data)
        hash_amount = len(share_data['entities']['hashtags'])
        if hash_amount > 2:
            rel = rel + (-0.1 * hash_amount)
        return rel

    def transform_share_kwargs(self, share):
        share = dict(share)
        coords = share.get('coordinates', False)
        if coords:
            location = Point(*coords.get('coordinates'))
        else:
            location = None
        # dubyateeeff
        # posted = arrow.get(
        #     share.get('created_at'), 'ddd MMM dd HH:mm:ss Z YYYY').datetime
        posted = datetime.strptime(
            share.get('created_at'), '%a %b %d %H:%M:%S +0000 %Y')
        new_share = {
            'network_id': share.get('id'),
            'user': share.get('user', {}).get('screen_name'),
            'text': share.get('text'),
            'location': location,
            'posted': posted
        }
        return new_share
