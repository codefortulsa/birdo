import re
from os import path
import json

from django.conf import settings
from django.db import transaction

from birds.models import Bird, PermutationType, BirdPermutation


def load_json(file=None):
    with open(file) as data_file:
        return json.load(data_file)


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
            # Don't recognize comma seperated, want to pull this int the re
            if permutations and ',' in permutations:
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
            # permutations should only be added if the bird model
            # already exists
            if permutations and not created:
                permutations = permutations.split('/')
                bird_perm = BirdPermutation.objects.create(
                    bird=bird_model,
                    vispedia_id=vispedia_id)
                for perm in permutations:
                    the_perm, created = PermutationType.objects.get_or_create(
                        name=perm)
                    bird_perm.types.add(the_perm)
                bird_perm.save()
            # add parent bird if not already added and available
            if created and not bird_model.parent and parent_id:
                try:
                    bird_model.parent = Bird.objects.get(vispedia_id=parent_id)
                except Bird.DoesNotExist:
                    pass
            bird_model.save()
