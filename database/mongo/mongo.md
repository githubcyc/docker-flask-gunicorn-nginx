
## mongo

```bash
docker-compose exec mongo_rs1 mongo
> use test
> db.test.insert({msg: "from master", ts: new Date()})
> db.test.find()

docker-compose exec mongo_rs2 mongo
> rs.slaveOk()  // set it Ok
> db.test.find()

docker-compose down

```

## Refer

* [mongodb主从备份 和 手动主从切换](https://www.cnblogs.com/amoyzhu/p/7943018.html)
* [基于 Docker 的 MongoDB 主从集群](https://zhuanlan.zhihu.com/p/42836964)
* :star:[bitnami/bitnami-docker-mysql: Bitnami MySQL Docker Image](https://github.com/bitnami/bitnami-docker-mysql)
* [sameersbn/docker-postgresql: Dockerfile to build a PostgreSQL container image which can be linked to other containers.](https://github.com/sameersbn/docker-postgresql)
* [bitnami/bitnami-docker-mongodb: Bitnami MongoDB Docker Image](https://github.com/bitnami/bitnami-docker-mongodb)