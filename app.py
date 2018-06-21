from flask import Flask
from flask_restful import Resource, Api, reqparse
from resources.predict import Predict
from resources.machine import Model

app = Flask(__name__)
api = Api(app)

predictor = Model()
api.add_resource(Predict, '/predict', '/', resource_class_kwargs={'model':predictor})
class Basic(Resource):
    def get(self):
        return {"CLASS": "Basic"}

api.add_resource(Basic, '/' )

if __name__ == '__main__':
    app.run(debug=True)