FROM postgis/postgis:latest
RUN apt-get update
RUN apt-get install -y postgis

ADD ./files/data.sql /docker-entrypoint-initdb.d