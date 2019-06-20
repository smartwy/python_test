#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    demo.py
#Login:     Administrator
#Descripton:
#Author:    Smartwy
#Date:      2019/6/10 14:36:27
#Version:

from flask import Flask
from flask_restful import reqparse,abort,Api,Resource
# Resource类将封装好了http的各种请求

app = Flask(__name__)
api = Api(app)

TODOS = {
	't1': {'task': 't1,manages'},
	't2': {'task': 't2,manages'},
	't3': {'task': 't3,manages'},
}

def id_exist(todo_id):
	if not todo_id in TODOS:
		abort(404, message="todo {} doesn`t exist".format(todo_id))

# 支持请求时携带变量名称，？分隔，&链接变量，如：http://127.0.0.1:5000/xueya?user_id=100&low=90&hig=120
parser = reqparse.RequestParser()
parser.add_argument('task')

class Todo(Resource):
	def get(self, todo_id):
		id_exist(todo_id)
		return TODOS[todo_id]

	def delete(self, todo_id):
		id_exist(todo_id)
		del TODOS[todo_id]
		return '', 204

	def put(self, todo_id):
		args = parser.parse_args()
		task = {'task':args['task']}
		TODOS[todo_id] = task
		return task, 201

class Todolist(Resource):
	def get(self):
		return TODOS

	def post(self):
		args = parser.parse_args() # 获取的from-data
		# print(args)
		todo_id = int(max(TODOS.keys()).lstrip('todo'))+1
		todo_id = 't%i' % todo_id
		TODOS[todo_id] = {'task': args['task']}
		return TODOS[todo_id],201

api.add_resource(Todo, '/todos/<todo_id>') # 查，删，更
api.add_resource(Todolist, '/todos') # 查 增

if __name__ == '__main__':
	app.run(debug=True)
