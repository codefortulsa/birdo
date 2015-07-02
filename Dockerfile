FROM python:2.7

RUN mkdir /app

# Set working dir
WORKDIR /app
COPY . /app

RUN apt-get update
RUN apt-get install -y \
  gcc \
  # python-gdal \
  libgdal-dev \
  libgeos-dev \
  swig \
  npm \
  nodejs

## Node setup, runs postinstall script in package.json
RUN npm install

## Django setup

# install requirements
RUN pip install gunicorn
RUN pip install -r requirements.txt

# RUN python manage.py migrate --noinput
# RUN python manage.py collectstatic --noinput

# build include paths env
ENV C_INCLUDE_PATH /usr/include/gdal/
ENV CPLUS_INCLUDE_PATH /usr/include/gdal/

# static/media dirs
VOLUME /app/static
VOLUME /app/media

# expose our gunicorn port
EXPOSE 5000

CMD ['gunicorn', 'birdo.wsgi:application', '-b', '0.0.0.0:5000', '--log-level=debug', '--error-logfile', '-']
