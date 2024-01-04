
##### Pasos para instalar el proyecto en tu computadora
Para esto es necesario tener instalado:
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

```
docker exec table_to_shape.web python manage.py migrate
```

Entro en la siguiente uri
```
 http://127.0.0.1:8000
```


Para crear un superusuario
```
docker exec -ti table_to_shape.web /bin/bash
python manage.py createsuperuser
```