
## sanic

```
pip install sanic
# 如果不想使用uvloop和ujson 可以这样安装
SANIC_NO_UVLOOP=true SANIC_NO_UJSON=true pip install sanic
```

## ORM

```
pip install --pre peewee-async; pip install aiomysql

//https://hub.docker.com/_/mysql/
docker run --name mysql -p 3306:3306 -v ~/mysql:/etc/mysql/conf.d \
-e MYSQL_ROOT_PASSWORD=123 -d mysql
docker exec -ti mysql bash
> mysql -u root -p 123
> show databases;
> create database test;
> drop database test;
> mysql -h 127.0.0.1 -u root －p 123
```

## Refer

* [Sanic — Sanic 0.7.0 documentation](https://sanic.readthedocs.io/en/latest/)
* [Sanic-For-Pythoneer/examples · howie6879/Sanic-For-Pythoneer](https://github.com/howie6879/Sanic-For-Pythoneer/tree/master/examples)
* [05bit/peewee-async: Asynchronous interface for peewee ORM powered by asyncio](https://github.com/05bit/peewee-async)
* [flask](https://github.com/project-hopkins/Westworld/tree/11694faed3c4d39202154e31dba2cd70c991f9be)