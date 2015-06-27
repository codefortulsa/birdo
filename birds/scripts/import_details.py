import requests


from birds.models import Bird

update = False

def run():
    birds = Bird.objects.leafs()
    for bird in birds:
        print("looking up details for bird {}".format(bird))
        if (update or not bird.details) and bird.vispedia_id:
            bird_endpoint = requests.get(bird.vispedia_url)
            if bird_endpoint.status_code == 200:
                print("got details, saving...")
                bird.details = bird_endpoint.json()
                bird.save()

        for perm in bird.permutations.all():
            if (update or not perm.details) and perm.vispedia_id:
                perm_endpoint = requests.get(perm.vispedia_url)
                if perm_endpoint.status_code == 200:
                    print("got perm details, saving...")
                    perm.details = perm_endpoint.json()
                    perm.save()
