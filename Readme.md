#Birdo

Scrape social networks for information about birds

##Installation

* make a virtualenv
* `$ pip install -r requirements.txt`
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
