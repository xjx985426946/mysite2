import flask
import json
from Configure.Mysql import MySqlConnection
from flask import Flask,render_template,request
import time

server = flask.Flask(__name__)

@server.route('/index', methods=['get'])
def index():
    res = {'msg': 'this is first api', 'msg_code': 0}
    return json.dumps(res, ensure_ascii=False)

@server.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_name = flask.request.values.get('user_name')
        password = flask.request.values.get('password')

        helper = MySqlConnection()
        ins = helper.select_one('select * from test_user where user_name=%s and password=%s', [user_name, password])

        if ins:
            return 'Hello OK'
        else:
            print('登录失败，请重新登录！')


server.run(port=6666, debug=True, host='127.0.0.1')