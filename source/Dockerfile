# https://github.com/OSGeo/gdal/tree/master/docker
FROM osgeo/gdal:ubuntu-small-latest

RUN echo "<97433> +proj=tmerc +lat_0=-34.629269 +lon_0=-58.463300 +k=0.999998 +x_0=100000 +y_0=100000 +ellps=intl +units=m +no_defs <>" >> /usr/share/proj/epsg 

# suprimo las advertencias de actualización de pip
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# python no intentará escribir archivos de bytes .pyc al importar módulos fuente
# no se guardará versiones compliladas de los modulos en el disco
ENV PYTHONDONTWRITEBYTECODE 1

# modo sin buffer, la salida se envia inmediatamente a la terminal sin almacenarse
# temporalmente en el buffer
ENV PYTHONUNBUFFERED 1

ENV PYTHONIOENCODING utf8


# Actualiza la lista de paquetes e instala dependencias
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    && apt-get install -y python3.pip python3-dev\
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 --no-cache-dir install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*


# Crea un usuario no root
RUN useradd -ms /bin/bash gisuser

# Cambia al usuario creado
USER gisuser

# Variables de entorno para evitar problemas de codificación
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# espacio de trabajo en donde se encontrará el código del proyecto
WORKDIR /usr/src/source


# copio el requirements.txt en la carpeta definida en WORKDIR
COPY ./requirements.txt . 

# instalo las librerias del proyecto
RUN pip install -r requirements.txt 

# copio todo el contenido que hay en el directorio source en la
# carpeta definida en WORKDIR
COPY . .