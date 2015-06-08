import time

from shares.networks import networks

from birds.models import Bird


def run():
    birds = Bird.objects.leafs()[50:]
    for Network in networks:
        network = Network()
        for bird in birds:
            network.grab_bird(bird)
            time.sleep(2)
