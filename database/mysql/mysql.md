
## mysql

* start

```bash
docker-compose up -d

docker exec -ti mysql_master bash
mysql -u root -p -h 127.0.0.1 -P 3306
show databases;
CREATE DATABASE test;
use test;
create table test(id int not null, name varchar(100));
insert into test values(1, 'from master');
select * from test;
```

* master config

```bash
docker exec -ti mysql_master bash

# install vim
apt-get update
apt-get install vim -y

vi /etc/mysql/my.cnf

# 默认同步全部数据库
[mysqld]
# 开启binary log并指定binary log的文件名前缀为mysql-bin
log-bin=mysql-bin
# 设置master机器的ID
server-id=1

/etc/init.d/mysql start
/etc/init.d/mysql restart
```

* replica config 
```bash
docker exec -ti mysql_replica bash
mysql -u repl -p -h mysql_master -P 3306
> SHOW SLAVE STATUS\G
> SHOW MASTER STATUS\G

docker logs -ft mysql_configure
mysql -u root -p -h mysql_master -P 3306
vim /etc/mysql/my.cnf

[mysqld]
# relay_log配置中继日志
relay_log=replicas-mysql-relay-bin 
server-id=2
replicate-do-table=test.test #database.table
master_host=master
master_port=3306
master_user=repl
master_password=repl
master_log_file=mysql-bin.000001
```


## Refer

* [MySQL :: MySQL 8.0 Reference Manual :: 17.1.6.3 Replication Slave Options and Variables](https://dev.mysql.com/doc/refman/8.0/en/replication-options-slave.html#option_mysqld_replicate-do-table)
* [使用 Docker Compose 搭建 MySQL 数据库主从复制实例](https://www.tomczhen.com/2017/12/11/deploy-mysql-replication-with-docker-compose/)
* [Docker Compose搭建MySQL主从复制集群](https://juejin.im/post/5b3a24dde51d4555b3360253)