# 导入Flask框架，这个框架可以快捷地实现了一个WSGI应用
from flask import Flask
# 默认情况下，flask在程序文件夹中的templates子文件夹中寻找模块
from flask import render_template
# 导入前台请求的request模块
from flask import request, session
from Configure.Mysql import MySqlConnection
# 引入wtf表单
from wtforms import PasswordField, StringField, Form
#引入表单验证器
from wtforms.validators import DataRequired

from Configure.Mysql import MySqlConnection

# 传递根目录
app = Flask(__name__)
app.secret_key = 'some_secret'

app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jps', 'jpeg', 'gif'}


user_nameSql = MySqlConnection().select_one('select user_name from test_user where user_name = %s')

# 默认路径访问登录页面
@app.route('/login', methods=['POST'])
def login():
    if user_nameSql != "N/A":
        print('登录失败')
        name = request.form.get('user_name')
        session['user_name'] = name

    else:
        print('登录成功')

@app.route('/login_in', methods=['POST'])
def login_in():
    name = request.form.get('user_name')
    session['user_name'] = name
    return session

if __name__ == '__main__':
    app.run(debug=True)