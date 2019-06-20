# -*- coding:utf-8 -*-
#Name:     
#Descripton:
#Author:    smartwy
#Date:     
#Version:

from flask import request,Flask,render_template,current_app,abort
from flask.views import MethodView # 用来支持CBV

app = Flask(__name__, template_folder='templates') # 这是实例化一个Flask对象，最基本的写法
# 但是Flask中还有其他参数，以下是可填的参数，及其默认值
# def __init__(self, import_name, static_path=None, static_url_path=None,
#                  static_folder='static', template_folder='templates',
#                  instance_path=None, instance_relative_config=False,
#                  root_path=None):

# template_folder：模板所在文件夹的名字, 默认就是templates
# root_path：可以不用填，会自动找到，当前执行文件，所在目录地址
# 在return render_template时会将上面两个进行拼接，找到对应的模板地址
# static_folder：静态文件所在文件的名字，默认是static，可以不用填
# static_url_path：静态文件的地址前缀，写成什么，访问静态文件时，就要在前面加上这个
# instance_path和instance_relative_config是配合来用的、
# 这两个参数是用来找配置文件的，当用app.config.from_pyfile('settings.py')这种方式导入配置文件的时候会用到
# instance_relative_config：默认为False，当设置为True时，from_pyfile会从instance_path指定的地址下查找文件。
# instsnce_path：指定from_pyfile查询文件的路径，不设置时，默认寻找和app.run()的执行文件同级目录下的instance文件夹；
# 如果配置了instance_path（注意需要是绝对路径），就会从指定的地址下里面的文件

# @app.route('/user/<username>')   #常用的   不加参数的时候默认是字符串形式的
# @app.route('/post/<int:post_id>')  #常用的   #指定int，说明是整型的
# @app.route('/post/<float:post_id>')
# @app.route('/post/<path:path>')
# @app.route('/login', methods=['GET', 'POST'])

# @app.route('/',methods=['GET','POST'])
class home(MethodView):   # CBV 模式
	def get(self):
		print(current_app.config)
		return render_template('home.html')
	def post(self):
		abort(404)

app.add_url_rule('/', view_func=home.as_view('home'), methods=['GET','POST'])
# app.add_url_rule('/***/<name>/', view_func=method, methods=['GET']) 示例

@app.route('/login',methods=['GET'])
def login_form():
	return render_template('form.html')

@app.route('/login',methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == '123456':
		return render_template('login_ok.html', username=username)
	# abort(404) # 触发404错误
	return render_template('form.html', message='Bad username or password', username=username)

# @app.errorhandler(404) # 404页面钩子
# def page_404(er): # 自定义404页面
# 	# print(er)
# 	return '404 error ...',404,{}

if __name__ == '__main__':
	app.run(debug=True)


