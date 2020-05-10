from flask import Flask
from flask_restful import Resource, Api, reqparse
import random
from random import seed
from random import randint
from flask import render_template
from werkzeug.wrappers import BaseResponse

app = Flask(__name__)
api = Api(app)

Tasks = [{'id':0,'need_to_do':{'name': 'Code', 'date': '12-03-2020', 'severity': '5'}}]


class todoList(Resource):
    
    def get(self):
        return Tasks

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

        need_to_do={}
        task['id']=random.randint(1,100)

        need_to_do['name']=args['name']
        need_to_do['date']=args['date']
        need_to_do['severity']=args['severity']

        task['need_to_do']= need_to_do

        Tasks.append(task)

        return{'task':task}

class todo(Resource) :
    def get(self,id):
        for task in Tasks:
            if int(task['id']) == int(id):
                return task


    def put(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True,
                            help='Name cannot be empty')
        parser.add_argument('date', type=str, required=True,
                            help='Please enter a date')
        parser.add_argument('severity', type=int, required=True,
                            help='Enter  a number between 1-5')
        args = parser.parse_args()
        for task in Tasks:
            if int(task['id']) == int(id):
                return tasks
        
            need_to_do=[]
            task['name']=args['name']
            task['date']=args['date']
            task['severity']=args['severity']
        return{'task':task}

    def delete(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str,
                            help='Name cannot be empty')
        parser.add_argument('date', type=str,
                            help='Please enter a date')
        parser.add_argument('severity', type=int,
                            help='Enter  a number between 1-5')
        args = parser.parse_args()
        for task in Tasks:
            if int(task['id']) == int(id):
                Tasks.remove(task)
        return Tasks
        


api.add_resource(todoList, '/')
api.add_resource(todo, '/todo/<id>')


class Response(BaseResponse):
   status = 200
   mimetype = "text/html"






if __name__ == '__main__':
    app.run(debug=True, port='5050')