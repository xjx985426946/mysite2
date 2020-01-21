import pymysql
import hashlib

class MySqlConnection(object):

    def __init__(self):
        self.host = '120.27.0.81'
        self.user = 'work'
        self.password = 'Work:2019'
        self.database = 'auto_test'

    # 数据库配置
    def connect(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,     # IP地址
                user=self.user,            # 用户名
                passwd=self.password,     # 密码
                database=self.database    # 数据库
            )
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        except:
            print("连接失败")
            return False

    # 查询一条数据
    def select_one(self, sql, params=None):
        '''
        根据sql和参数获取一行数据
        :param sql: sql语句
        :param params: sql语句对象的参数元组，默认值为None
        :return: 查询的一行数据
        '''
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as ex:
            print(ex)
        return result

    # 查询多条数据
    def select_all(self, sql, params=None):
        '''
        根据sql和参数获取一行数据
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 查询的一行数据
        '''
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as ex:
            print(ex)
        return result

    def __item(self, sql, params=None):
        '''
        执行增删改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as ex:
            print(ex)
        return count

    def update(self, sql, params=None):
        '''
        执行修改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    def insert(self, sql, params=None):
        '''
        执行新增
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    def delete(self, sql, params=None):
        '''
        执行删除
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__item(sql, params)

    def my_md5(self, pwd):
        my_md5 = hashlib.md5()
        my_md5.update(pwd.encode('utf-8'))
        return my_md5.hexdigest()

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    sql = 'select * from test_user where user_name=\'test\' and password=\'123\';'
    data = MySqlConnection().select_one(sql)
    print(data)
