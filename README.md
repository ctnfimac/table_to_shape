# Tablas a Archivos Geográficos
Este proyecto tiene como objetivo que un usuario pueda conectarse a una base de datos y descargar la información de una o más tablas en formatos .shp .cpg .dbf .prj .shx 

### Tecnologías Utilizadas
- Docker | Docker-Compose
- Python | Django 
- Postgres | Postgis
- Html | Css | Javascript



### :package: Instalación
Programas necesarios:
- [Git](https://git-scm.com/) 
- [Docker](https://www.docker.com/) 
- [Docker compose](https://docs.docker.com/compose/) 


Ejecutar los siguientes comandos desde una terminal

```
git clone https://github.com/ctnfimac/table_to_shape.git
```

```
cd  table_to_shape/
```

```
docker-compose up [-d]
```

**Importante**: las tablas tienen que tener un campo **geom**

## :computer: Uso

1) Ingreso a la siguiente uri
    ```
    http://127.0.0.1:8000/web/
    ```
2) Completo las credenciales en el formulario o uso las que vienen por defecto
3) Elijo el Esquema
4) Selecciono una o varias tablas
5) Click en el botón verde de Descargar
6) Puedo visualizarlos de forma gráfica con [Qgis](https://qgis.org/es/site/) o [Mapshaper](https://mapshaper.org/)

Ejemplo de visualización con Qgis de los archivos generados:
![Qgis con capas](https://github.com/ctnfimac/table_to_shape/blob/main/source/static/img/muestra.png?raw=true)

Interfaz del usuario
![Usuario](https://github.com/ctnfimac/table_to_shape/blob/main/source/static/img/usuario.jpeg?raw=true)

## Pruebas Unitarias
```
docker exec table_to_shape.web python manage.py test web.views.tests.test_conection
```
```
docker exec table_to_shape.web python manage.py test web.utils.tests.test_database_conection
```
```
docker exec table_to_shape.web python manage.py test web.utils.tests.test_table_to_shape_actions
```


## :slightly_smiling_face: Autor
Christian Peralta :arrow_right: [Linkedin](https://www.linkedin.com/in/christianperalta87/)
