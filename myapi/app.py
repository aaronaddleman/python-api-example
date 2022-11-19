"""Main application file for the program."""

from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    """Represent users for the appliction."""

    def get(self):
        """Get a user from a data source."""
        data = pd.read_csv('users.csv')
        data = data.to_dict()
        return {'data': data}


class Locations(Resource):
    """Register locations."""

    pass


api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    app.run()
