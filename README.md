# docker-flask-gunicorn-nginx
Bootstrap example of a Flask/Dash app served via Gunicorn and Nginx using Docker containers

Guildeline article can be found at https://sladkovm.github.io/webdev/2017/10/16/Deploying-Plotly-Dash-in-a-Docker-Container-on-Digitital-Ocean.html

### Run

/bin/bash run_docker.sh

1. It will kill all running docker processes.
2. Will start all required containers in background

### In your browser (assuming the docker-machine runs on 192.168.99.100)

http://192.168.99.100

## uWSGI

```
uwsgi --http 127.0.0.1:5000 --module myproject:app
```
* [Standalone WSGI Containers — Flask 1.0.2 documentation](http://flask.pocoo.org/docs/1.0/deploying/wsgi-standalone/#uwsgi)
* [tiangolo/full-stack: Full stack, modern web application generator. Using Flask, Docker, Swagger, automatic HTTPS and more...](https://github.com/tiangolo/full-stack)
* :star:[flask-api: flask-restful api manager](https://github.com/V-I-C-T-O-R/flask-api)
* [dracarysX/flask_restapi: Flask restAPI framework. Python、Flask、APIMethodView、Filtering Query API](https://github.com/dracarysX/flask_restapi)
* [robpco/docker-nginx-uwsgi-flask: Docker image to quickly deploy Python Flask Web Apps on NGINX. Image includes Nginx, uWSGI, Python, and Flask](https://github.com/robpco/docker-nginx-uwsgi-flask)
* [squeaky-pl/japronto: Screaming-fast Python 3.5+ HTTP toolkit integrated with pipelining HTTP server based on uvloop and picohttpparser.](https://github.com/squeaky-pl/japronto)
* [xiiiblue/flask-rest-sample: REST API](https://github.com/xiiiblue/flask-rest-sample)
* [Flask-Potion is a RESTful API framework for Flask and SQLAlchemy, Peewee or `MongoEngine`](https://github.com/biosustain/potion)
