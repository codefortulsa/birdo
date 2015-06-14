import re
from os import path
import json

from django.conf import settings
from django.db import transaction

from birds.models import Bird, PermutationType, BirdPermutation


def load_json(file=None):
    with open(file) as data_file:
        return json.load(data_file)


# TODO, when a 2nd level nesting to split on comma, and trim all permutation names
def run():
    birds = load_json(
        path.os.path.normpath(
            settings.BASE_DIR + '/fixtures/vispedia-birds.json'))
    # remove the root bird element
    birds = birds[1:]
    perm_pattern = re.compile(r'(\w.*)\s?\((.*?)\)')
    with transaction.atomic():
        for bird in birds:
            permutations = None
            vispedia_id = bird.get('external_id')
            parent_id = bird.get('parent', False)
            name = bird.get('name')
            found_name = None
            found_permutation = perm_pattern.match(name)
            if found_permutation:
                found_name, permutations = found_permutation.groups()
            # if the parent is the root, it's a category
            if parent_id == 'XMvTNcmDmF4ZbZJBtndZLM':
                permutations = None
                found_name = None
            if found_name:
                bird_model = Bird.objects.get(vispedia_id=parent_id)
                created = False
            else:
                bird_props = {
                    'name': name,
                    'order': int(bird.get('order')),
                }
                bird_model, created = Bird.objects.get_or_create(
                    vispedia_id=vispedia_id, defaults=bird_props)
            # split off permutations
            print(bird_model)
            if permutations:
                # split on
                permutations = re.split(r'[,/]+', permutations)
                # always create a new permutations for this vispedia ID
                bird_perm = BirdPermutation.objects.create(
                    bird=bird_model,
                    vispedia_id=vispedia_id)
                for perm in permutations:
                    perm = perm.lower().strip()
                    the_perm, pcreated = PermutationType.objects.get_or_create(
                        name=perm)
                    if pcreated:
                        print('creating perm type {}'.format(the_perm))
                    print('assigning perm type {} to {}'.format(the_perm, bird_perm))
                    bird_perm.types.add(the_perm)
                bird_perm.save()
            # add parent bird if not already added and available
            if created and not bird_model.parent and parent_id:
                try:
                    bird_model.parent = Bird.objects.get(vispedia_id=parent_id)
                except Bird.DoesNotExist:
                    pass
            bird_model.save()
