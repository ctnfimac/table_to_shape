# Tablas a Archivos Geográficos
Este proyecto tiene como objetivo que un usuario pueda conectarse a una pase de datos Postgres/Postgis y descargar la información de una o más tablas en formatos .shp .cpg .dbf .prj .shx 

### :package: Pasos para instalar el proyecto  
Es necesario tener instalado:
- [Git](https://git-scm.com/) 
- [Docker](https://www.docker.com/) 
- [Docker compose](https://docs.docker.com/compose/) 


Ejecutar los siquientes comandos desde la terminal
```
git clone https://github.com/ctnfimac/table_to_shape.git
```


```
cd  table_to_shape/
```

```
docker-compose up [-d]
```


*Me conecto al contenedor de la base de datos*
```
docker exec -ti table_to_shape.database bash
```

*Genero las tablas de prueba con sus respectivos datos*
```
shp2pgsql -I -s EPSG:4326 -W "latin1" /data/Recorridos_MTB_SEP23.shp public.recorridos | psql -h 127.0.0.1 -p 5432 -d gis -U gis
```
```
shp2pgsql -I -s EPSG:4326 -W "latin1" /data/techos_inteligentes_verdes_WGS84.shp public.techos_inteligentes | psql -h 127.0.0.1 -p 5432 -d gis -U gis
```
```
shp2pgsql -I -s EPSG:4326 -W "latin1" /data/barrios_wgs84.shp public.barrios | psql -h 127.0.0.1 -p 5432 -d gis -U gis
```
**Importante!!**: las tablas tienen que tener el campo **geom**

## :computer: Uso

1) Entro en la siguiente uri
    ```
    http://127.0.0.1:8000/web/
    ```
2) Completo las credenciales en el formulario o uso las que vienen por defecto
3) Elijo el Esquema
4) Elijo una o varias tablas
5) Click en el boton verde de Descargar
6) Puedo visualizarlos de forma gráfica con [Qgis](https://qgis.org/es/site/) o [Mapshaper](https://mapshaper.org/)

Ejemplo de visualización con Qgis de los archivos generados:
![Qgis con capas](https://github.com/ctnfimac/table_to_shape/blob/main/source/static/img/muestra.png?raw=true)

## :slightly_smiling_face: Autor
Christian Peralta :arrow_right: [Linkedin](https://www.linkedin.com/in/christianperalta87/)


## Pruebas Unitarias
Para ejecutarlas corra los siguientes comandos
```
docker exec table_to_shape.web python manage.py test web.views.tests.test_conection
```
```
docker exec table_to_shape.web python manage.py test web.utils.tests.test_database_conection
```
```
docker exec table_to_shape.web python manage.py test web.utils.tests.test_table_to_shape_actions
```