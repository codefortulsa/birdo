import requests


from birds.models import Bird


def run():
    birds = Bird.objects.leafs().filter(vispedia_id__isnull=False)
    for bird in birds:
        print("looking up details for bird {}".format(bird))
        bird_endpoint = requests.get(bird.vispedia_url)
        if bird_endpoint.status_code == 200:
            print("got details, saving...")
            bird.details = bird_endpoint.json()
            bird.save()
