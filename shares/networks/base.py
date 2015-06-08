from django.utils.timezone import now

from shares.models import Share, BirdSearchResult
from birds.models import Bird


class BirdKeywordMixin(object):
    bird_keywords = [
        'bird', 'birds', 'birder', 'watching', 'birding', 'outdoors',
        'sky', 'watch', 'flying', 'flight', 'feeding', 'nest',
        'nesting', 'ornithology', 'pond']
    negative_keywords = [
        'buy', 'bar', '$', 'out', 'hot', 'eat', 'dinner', 'club',
        'tap', 'drink', 'cream', 'ale', 'free', 'drinking', 'tavern']
    full_bird_names = []
    all_keywords = []

    def __init__(self, *args, **kwargs):
        super(BirdKeywordMixin, self).__init__(*args, **kwargs)
        self.build_bird_keywords()

    def build_bird_keywords(self):
        for bird in Bird.objects.leafs():
            self.full_bird_names.append(bird.name)
            [self.bird_keywords.append(keyword)
             for keyword in bird.name.split(' ')]
        # words = self.full_bird_names + self.bird_keywords
        # self.all_keywords = [
        #     e for i, e in enumerate(words) if words.index(e) == i]

    def calculate_relevance(self, share_model, share_data):
        rel = super(BirdKeywordMixin, self).calculate_relevance(
            share_model, share_data)
        text = share_model.text.lower()

        for word in self.bird_keywords:
            if word.lower() in text:
                rel += 0.15

        for name in self.full_bird_names:
            if name.lower() in text:
                rel += 0.30

        for bad in self.negative_keywords:
            if bad.lower() in text:
                rel -= 0.20

        return rel


class Network(object):

    """
    Generic network interface for searching social shares
    for tags and words
    """

    model = Share
    network_type = model.UNKNOWN

    def __init__(self, *args, **kwargs):
        self.api = self.init_api(**kwargs)

    def init_api(self, **kwargs):
        raise NotImplementedError

    def calculate_relevance(self, share_model, share_data):
        """
        Estimate how much this share relates to our subject
        """
        share_model.rel_lastrun = now()
        return 0.2

    def create_share(self, share):
        share_kwargs = self.transform_share_kwargs(share)
        return self.model.objects.get_or_create(
            network_id=share_kwargs.pop('network_id'),
            network=self.network_type,
            defaults=share_kwargs)

    def transform_share_kwargs(self, share):
        raise NotImplementedError

    def search_social_shares(self, prev_results, search_query):
        raise NotImplementedError

    def grab_bird(self, bird):

        try:
            prev_results = BirdSearchResult.objects.filter(
                target_bird=bird).latest()
        except BirdSearchResult.DoesNotExist:
            prev_results = None

        search_query = bird.name

        meta, social_shares = self.search_social_shares(
            prev_results, search_query)
        print('found {} social shares for {}'.format(
            len(social_shares), search_query))

        self.create_search_results(bird, meta)

        # exit early if nothing to do
        if not len(social_shares) > 0:
            return

        for social_share in social_shares:
            new_share, created = self.create_share(social_share)
            if new_share:
                new_share.rel = self.calculate_relevance(
                    new_share, social_share)
                new_share.birds.add(bird)
                new_share.save()
                print(new_share, created)

    def create_search_results(self, meta):
        raise NotImplementedError
