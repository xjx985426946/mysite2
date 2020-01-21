import flask
import json
from Configure.Mysql import MySqlConnection
from flask import Flask, render_template, request, make_response, jsonify
import time
from flask_cors import *

server = flask.Flask(__name__)
CORS(server, resources=r'/*')

# @server.route('/')
# @server.route('/index')
# def index():
#     # res = {'msg': 'this is first api', 'msg_code': 0}
#     # return json.dumps(res, ensure_ascii=False)
#     user = {'username': 'auto_test'}
#     return render_template('login.html', title='自动化测试平台', user=user)

@server.route('/login', methods=['POST'])
def login():
    return_dirt = {'code': '300', 'return_info': '处理成功', 'results': False}
    login_data = request.get_data()
    login_data2 = json.loads(login_data)
    name = login_data2.get('user_name')
    pwd = login_data2.get('password')

    if name == '' or pwd == '':
        return_dirt['code'] = '5001'
        return_dirt['return_info'] = '登录失败，请输入用户名或密码！'
        print(return_dirt)
        res = make_response(json.dumps(return_dirt))
        return res

    else:
        helper = MySqlConnection()
        ins = helper.select_one('select * from test_user where user_name=%s and password=%s;', [name, pwd])
        print(ins)
        if ins:
            return_dirt['return_info'] = '登录成功！'
            return_dirt['results'] = 'True'
            return_dirt['code'] = '200'
            print(return_dirt)
            res = make_response(json.dumps(return_dirt))
            return res
        else:
            return_dirt['return_info'] = '登录失败！请输入正确的用户名和密码'
            return_dirt['code'] = '400'
            print(return_dirt)
            res = make_response(json.dumps(return_dirt))
            return res


@server.route('/register', methods=['POST'])
def register():
    return_dirt = {'code': '200', 'return_info': '处理成功', 'results': False}
    login_data = request.get_data()
    login_data2 = json.loads(login_data)
    name = login_data2.get('user_name')
    pwd = login_data2.get('password')
    if name == '' or pwd == '':
        return_dirt['code'] = '5001'
        return_dirt['return_info'] = '注册失败，请输入用户名或密码！'
        return json.dumps(return_dirt, ensure_ascii=False)

    else:
        print(return_dirt)
        helper = MySqlConnection()
        ins = helper.insert('insert into test_user(user_name, password) values(%s,%s)', [name, pwd])

        if ins:
            return_dirt['return_info'] = '注册成功！'
            return_dirt['results'] = 'True'
            return json.dumps(return_dirt, ensure_ascii=False)

        else:
            return_dirt['return_info'] = '注册失败！'
            return_dirt['code'] = '400'
            return json.dumps(return_dirt, ensure_ascii=False)


# @server.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
#     # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
#     response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8088/login'
#     return response

if __name__ == '__main__':
    server.run(port=8000, debug=True)
