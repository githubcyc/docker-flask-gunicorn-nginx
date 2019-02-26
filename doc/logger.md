
## logrotate

```
yum install logrotate -y
apt-get install logrotate -y

// uwsgi.ini
#location of log files
logto = /var/log/uwsgi/%n.log

sudo mkdir -p /var/log/uwsgi
sudo chown -R user:user /var/log/uwsgi

vim /etc/logrotate.d/myapp

```

## Refer

* [uWSGI Options — uWSGI 2.0 documentation](https://uwsgi-docs.readthedocs.io/en/latest/Options.html?highlight=logto#logto)