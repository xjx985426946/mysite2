import flask
import json
from Configure.Mysql import MySqlConnection
from flask import Flask, render_template, request
import time

server = flask.Flask(__name__)

@server.route('/')
@server.route('/index')
def index():
    # res = {'msg': 'this is first api', 'msg_code': 0}
    # return json.dumps(res, ensure_ascii=False)
    user = {'username': 'auto_test'}
    return render_template('login.html', title='自动化测试平台', user=user)

@server.route('/login', methods=['POST'])
def login():
    return_dirt = {'code': '200', 'return_info': '处理成功', 'results': False}
    login_data = request.get_data()
    login_data2 = json.loads(login_data)
    name = login_data2.get('user_name')
    pwd = login_data2.get('password')
    if name == '' or pwd == '':
        return_dirt['code'] = '5001'
        return_dirt['return_info'] = '登录失败，请输入用户名或密码！'
        return json.dumps(return_dirt, ensure_ascii=False)

    else:
        print(return_dirt)
        helper = MySqlConnection()
        ins = helper.insert('select * from test_user where user_name=%s and password=%s', [name, pwd])
        if ins:
            return_dirt['return_info'] = '登录成功！'
            return_dirt['results'] = 'True'
            return json.dumps(return_dirt, ensure_ascii=False)
        else:
            return_dirt['return_info'] = '登录失败！请输入正确的用户名和密码'
            return_dirt['code'] = '400'
            return json.dumps(return_dirt, ensure_ascii=False)


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


if __name__ == '__main__':
    server.run(port=6668, debug=True)
