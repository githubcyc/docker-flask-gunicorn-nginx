
## redis的主从复制，读写分离，主从切换

### 主从切换

> 当数据量变得庞大的时候，`读写分离`还是很有必要的。同时避免一个redis服务宕机，导致应用宕机的情况，我们启用sentinel(哨兵)服务，实现`主从切换`的功能。

* 准备三个redis服务，依次命名文件夹子master,replica1,replica2.
* 这里为在测试机上，不干扰原来的redis服务，我们master使用6000端口。

配置文件（redis.conf）
```
//master配置修改端口：

port 6000
requirepass 123456

// replica1修改配置 read only
port 6001
replicaof 127.0.0.1 6000
masterauth 123456
requirepass 123456

// replica2修改配置
port 6002
replicaof 127.0.0.1 6000
masterauth 123456
requirepass 123456
```
> requirepass是认证密码，应该之后要作主从切换，所以建议所有的密码都一致， masterauth是从机对主机验证时，所需的密码。（即主机的requirepass）

* start

```
// main-node
redis-server redis.conf 　

// sub-node
redis-server redis1.conf


ps -ef |grep redis

// check main-node
$ redis-cli -p 6000
127.0.0.1:6000> auth 123456
127.0.0.1:6000> set test ok

// check sub-node
redis-cli -p 6001
127.0.0.1:6001> auth 123456
127.0.0.1:6001> get test
"ok"

```
> 主机执行写命令，从机能同步主机的值，主从复制，读写分离.

### switch

> if main-node is down, 所以redis提供了一个sentinel（哨兵），以此来实现主从切换的功能，类似与zookeeper.

```
// config 2 sentinel
vi sentinel.conf 

port 26379
// 两个及以上的sentinel服务检测到master宕机，才会去执行主从切换的功能。
sentinel monitor mymaster 127.0.0.1 6000 2
sentinel auth-pass mymaster 123456

// vi sentinel.conf

port 26479
sentinel monitor mymaster 127.0.0.1 6000 2
sentinel auth-pass mymaster 123456

// start sentinel service
redis-server sentinel-1.conf --sentinel


// kill main
kill -9 <psid>
// master切换为6001，当6000端口的这个服务重启的时候，会变成6001端口服务的replica。

// 因为sentinel在切换master的时候，把对应的sentinel.conf和redis.conf文件的配置修改了。
```

## Refer

* [redis的主从复制，读写分离，主从切换](https://www.cnblogs.com/ruiati/p/6374145.html)
> Docker
* [bitnami/bitnami-docker-redis: Bitnami Redis Docker Image](https://github.com/bitnami/bitnami-docker-redis)
* [docker 搭建 redis 主从的 docker-compose.yml · TesterHome](https://testerhome.com/topics/13091)