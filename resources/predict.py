from flask_restful import Resource
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('Tweet', type=str, required=True)

class Predict(Resource):
    #Resource to predict the category of a tweet 
    def __init__(self, **kwargs):
        self.model = kwargs['model']
               
    def put(self):
        args = parser.parse_args()
        return {'category' : self.model.predict(args.Tweet)}

    def get(self):
        args = parser.parse_args()
        return {'category' : self.model.predict(args.Tweet)}