from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.predict import Predict
from resources.machine import Model

app = Flask(__name__)
api = Api(app)

predictor = Model()

class Basic(Resource):
    def get(self):
        return {"CLASS": "Basic"}

api.add_resource(Basic, '/' )
api.add_resource(Predict, '/predict', '/Predict', resource_class_kwargs={'model':predictor})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)