from os import path
import json

from django.conf import settings
from django.db import transaction

from birds.models import Bird


def load_json(file=None):
    with open(file) as data_file:
        return json.load(data_file)


def run():
    birds = load_json(
        path.os.path.normpath(
            settings.BASE_DIR + '/fixtures/vispedia-birds.json'))
    with transaction.atomic():
        for bird in birds:
            vispedia_id = bird.get('external_id')
            parent_id = bird.get('parent', False)
            bird_props = {
                'name': bird.get('name'),
                'order': int(bird.get('order')),
            }
            bird_model, created = Bird.objects.get_or_create(
                vispedia_id=vispedia_id, defaults=bird_props)
            # add parent bird if not alraedy added and avilable
            if not bird_model.parent and parent_id:
                try:
                    bird_model.parent = Bird.objects.get(vispedia_id=parent_id)
                except Bird.DoesNotExist:
                    pass
            bird_model.save()
