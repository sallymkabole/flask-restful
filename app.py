from flask import Flask
from flask_restful import Resource, Api, reqparse
import math
import random
from random import seed
from random import randint
app = Flask(__name__)
api = Api(app)

tasks = [{'id':0,'name': 'Code', 'date': '12-03-2020', 'severity': '5'}]


class todo(Resource):
    def get(self):
        return {'tasks': tasks}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True,
                            help='Name cannot be empty')
        parser.add_argument('date', type=str, required=True,
                            help='Please enter a date')
        parser.add_argument('severity', type=int, required=True,
                            help='Enter  a number between 1-5')
        args = parser.parse_args()
        task={}
        task['id']=random.randint(1,100)
        task['name']=args['name']
        task['date']=args['date']
        task['severity']=args['severity']
        tasks.append(task)
        return{'task':task}


api.add_resource(todo, '/')

if __name__ == '__main__':
    app.run(debug=True, port='5050')