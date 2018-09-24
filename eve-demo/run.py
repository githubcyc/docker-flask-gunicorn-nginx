# https://github.com/pyeve/eve-demo
from eve import Eve
from settings import DOMAIN
from eve.auth import BasicAuth
class MybasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == 'admin' and password == 'admin'
            

test = {
    'allow_unknown': True,
    'resource_methods': ['GET', 'POST']
}

config = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'test',
    'URL_PREFIX': 'api',
    'API_VERSION': 'v1',
    'DEBUG': True,
    'DOMAIN': DOMAIN,
}
app = Eve(settings=config, auth=None)

@app.route('/hello')
def hello():
    """ A Eve instance is still a 100% Flask application """
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/api/v1/test