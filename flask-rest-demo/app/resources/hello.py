from flask_restful import Resource, reqparse

class HelloWorld(Resource):
    def get(self):
        raise ValueError('d')
        return {'hello': 'world'}
    def post(self):
        r = reqparse.RequestParser()
        r.add_argument('test', type=str, required=True)
        r.parse_args()
        return {'d': 1}