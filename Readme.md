#Birdo

Scrape social networks for information about birds

##Installation

* make a virtualenv
* `$ pip install -r requirements/local.txt`
* install postgres >= 9.4
* install geos libraries
    * mac: `$ brew install geos`
    * more: https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/geolibs/
* install gdal libraries
    * mac: `# brew install gdal`
* create database
    * `$ createdb birdo`
    * more: https://docs.djangoproject.com/en/1.8/ref/contrib/gis/tutorial/
* sync database
    * `$ python manage.py migrate`
* build frontend
    * `$ cd assets`
    * `$ npm install && npm run build`

Run it:

`$ python manage.py runserver_plus`

## Fixtures

### Birds

Create bird models from vispedia data

```
$ python manage.py runscript import_birds
$ python manage.py runscript import_details
```


## Deploying

## With dokku!

```
cd /var/lib/dokku/plugins
sudo git clone https://github.com/rlaneve/dokku-link.git link
#sudo git clone https://github.com/fermuch/dokku-pg-plugin.git postgis
sudo git clone https://github.com/destos/dokku-pgis-plugin.git postgis
```

```
dokku config:set birdo NPM_CONFIG_PRODUCTION=true
dokku config:set birdo DJANGO_CONFIGURATION=Production DJANGO_SETTINGS_MODULE=config
dokku config:set birdo DJANGO_TWITTER_KEY='your twitter key'
dokku config:set birdo DJANGO_TWITTER_SECRET='your twitter secret'
dokku config:set birdo DJANGO_TWITTER_TOKEN='twitter token'
dokku config:set birdo DJANGO_TWITTER_TOKEN_SECRET='twitter token secret'
dokku config:set birdo DJANGO_SECRET_KEY='secret'
dokku config:set birdo DJANGO_DATABASES='postgis://root:password@172.17.42.1:32769/db'
dokku config:set birdo GEOS_LIBRARY_PATH='/app/.geodjango/geos/lib/libgeos_c.so'
dokku config:set birdo GDAL_LIBRARY_PATH='/app/.geodjango/gdal/lib/libgdal.so'
dokku config:set birdo PROJ4_LIBRARY_PATH='/app/.geodjango/proj4/lib/libproj.so'
dokku config:set birdo DJANGO_ADMINS=Terry,tjones@site.com;Another Person,gchapman@site.com
```

After Deploy

```
dokku run birdo python manage.py migrate
```
