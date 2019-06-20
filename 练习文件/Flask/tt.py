#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    python_test
#F-Name:    tt.py
#Login:     Administrator   
#Descripton:
#Author:    Smartwy
#Date:      2019/6/10 16:17:49
#Version:

from flask import Flask, abort, request, jsonify

app = Flask(__name__)

# 测试数据暂时存放
tasks = []

@app.route('/add_task/', methods=['POST'])
def add_task():
    print(request.json)
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        # 没有指定id则返回全部
        return jsonify(tasks)
    else:
        task_id = request.args['id'] # 取出id值
        task = list(filter(lambda t: t['id'] == int(task_id), tasks))  # 筛选请求id是否合法(在数据内)
        # print(task) # filter结果为内存地址，需要list转换，否则jsonify报错
        return jsonify(task) if task else jsonify({'result': 'not found'})

if __name__ == "__main__":
    # 将host设置为0.0.0.0，则外网用户也可以访问到这个服务
    app.run(port=8383, debug=True)


