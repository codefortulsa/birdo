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
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install
RUN npm run build

## Django setup

# static/media dirs
VOLUME /app/static
VOLUME /app/media

# install requirements
RUN pip install -r requirements.txt

# build include paths env
ENV C_INCLUDE_PATH /usr/include/gdal/
ENV CPLUS_INCLUDE_PATH /usr/include/gdal/

ENV GEOS_LIBRARY_PATH /usr/lib/libgeos_c.so
ENV GDAL_LIBRARY_PATH /usr/lib/libgdal.so

# expose our gunicorn port
EXPOSE 5000

CMD ./bin/start_app.sh
