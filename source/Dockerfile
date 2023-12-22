FROM python:3.8.3-slim-buster

# suprimo las advertencias de actualización de pip
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

# python no intentará escribir archivos de bytes .pyc al importar módulos fuente
# no se guardará versiones compliladas de los modulos en el disco
ENV PYTHONDONTWRITEBYTECODE 1

# modo sin buffer, la salida se envia inmediatamente a la terminal sin almacenarse
# temporalmente en el buffer
ENV PYTHONUNBUFFERED 1

# espacio de trabajo en donde se encontrará el código del proyecto
WORKDIR /usr/src/source

# actualizamos la herramienta pip en su última version disponible
RUN pip install --upgrade pip

# copio el requirements.txt en la carpeta definida en WORKDIR
COPY ./requirements.txt . 

# instalo las librerias del proyecto
RUN pip install -r requirements.txt 

# copio todo el contenido que hay en el directorio source en la
# carpeta definida en WORKDIR
COPY . .