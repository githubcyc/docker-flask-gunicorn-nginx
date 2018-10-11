

## mongo on docker

> [library/mongo - Docker Hub](https://hub.docker.com/_/mongo/)

```markdown
docker run --name mongo-test -d -p 27017:27017 -v $PWD/db:/data/db mongo:latest 
--config /etc/mongo/mongod.conf mongod --auth

docker exec -it mongo-test sh

mongo

// 切换到admin并创建root用户
use admin
db.createUser({ user: 'root', pwd: 'root', roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] })

db.auth("root", "root")
show users

// 拥有对数据库app的读写权限。
use app
db.createUser(
  {
    user: "app",
    pwd: "app",
    roles: [ { role: "readWrite", db: "app" }
             ]
  }
)


```

## mongo UI

[Robomongo](https://robomongo.org/download)

## Refer

1. [Flask-PyMongo — Flask-PyMongo 2.0.0b2.post13 documentation](http://flask-pymongo.readthedocs.io/en/latest/)