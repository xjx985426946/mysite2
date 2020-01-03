# 导入Flask框架，这个框架可以快捷地实现了一个WSGI应用
from flask import Flask
# 默认情况下，flask在程序文件夹中的templates子文件夹中寻找模块
from flask import render_template
# 导入前台请求的request模块
from flask import request
from Configure.Mysql import MySqlConnection
# 引入wtf表单
from wtforms import PasswordField,StringField,Form
#引入表单验证器
from wtforms.validators import DataRequired

class LoginForm(Form):
    Username = StringField("Username", validators=[DataRequired()])
    Password = PasswordField("Password", validators=[DataRequired])

# 传递根目录
app = Flask(__name__)
app.config.from_object('config')

# 默认路径访问登录页面
@app.route('/', method=['GET', 'POST'])
def login():
    form = loginform(request.form)
    return render_template('login.html')

# 默认路径访问注册页面
@app.route('/register')
def register():
    return render_template('register.html')

# # 获取登录参数及处理
# @app.route('/login_user')
# def get_login():
#     # SQL 查询语句
#     sql = "select * from user where user=" + request.args.get('user_name') + " and password=" + request.args.get(
#         'password') + ""
#     helper = MySqlConnection()
#     ins = helper.select_one(sql)
#     try:
#         # 执行sql语句
#         if ins:
#             return '登录成功'
#         else:
#             return '用户名或密码不正确'
#         # 提交到数据库执行
#     except:
#         return False
#
#
# # 获取注册请求及处理
# @app.route('/register_user')
# def register_user():
#     # SQL 插入语句
#     sql = "INSERT INTO user(user, password) VALUES ("+request.args.get('user')+", "+request.args.get('password')+")"
#     helper = MySqlConnection()
#
#     try:
#         helper.insert(sql)
#         return render_template('login.html')
#     except:
#
#         return '注册失败'

# 使用__name__ == '__main__'是 Python 的惯用法，确保直接执行此脚本时才
# 启动服务器，若其他程序调用该脚本可能父级程序会启动不同的服务器
if __name__ == '__main__':
    app.run(debug=True)