from Configure.Mysql import MySqlConnection

def register():
    name = input('请输入用户名：')
    password = input('请输入密码：')

    helper = MySqlConnection()

    ins = helper.insert('insert into test_user(user_name, password) values(%s,%s)', [name, password])
    if ins:
        print('注册成功！')
    else:
        print('注册失败，请重新注册！')

def login():
    name = input('请输入用户名：')
    password = input('请输入密码：')

    helper = MySqlConnection()
    ins = helper.select_one('select * from test_user where user_name=%s and password=%s', [name, password])

    if ins:
        print('登录成功')
    else:
        print('登录失败，请重新登录！')

def main():
    while True:
        choice = input('1、注册    2、登录\n请输入要进行的操作：')

        if choice == '1':
            register()
        elif choice == '2':
            login()
        else:
            print('请等待版本更新！')

if __name__ == '__main__':
    main()