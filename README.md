
##### Pasos para instalar el proyecto
Es necesario tener instalado:
- [Git](https://git-scm.com/) 
- [Docker](https://www.docker.com/) 
- [Docker compose](https://docs.docker.com/compose/) 


Ejecutar los siquientes comandos
```
git clone https://github.com/ctnfimac/table_to_shape.git
```


```
cd  table_to_shape/
```

```
docker-compose up [-d]
```


Entro en la siguiente uri
```
http://127.0.0.1:8000/web/
```


Para hacer las pruebas locales se genera una tabla y cargan los datos.(pedirá la contraseña de la base de datos)
```
docker exec table_to_shape.database shp2pgsql -I -s EPSG:4326 -W "latin1" /data/techos_inteligentes_verdes_WGS84.shp public.techos_inteligentes | psql -h 127.0.0.1 -p 5432 -d gis -U gis
```