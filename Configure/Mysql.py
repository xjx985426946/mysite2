import pymysql

class MySqlConnection(object):

    def __init__(self):
        self.get_conn()

    # 数据库配置
    def get_conn(self):
        try:
            self.conn = pymysql.connect(
                host='120.27.0.81',     # IP地址
                user='work',            # 用户名
                passwd='Work:2019',     # 密码
                database='auto_test'    # 数据库
            )
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

        except:
            # logger.error("connectDatabase failed")
            print("连接失败")
            return False

    # 查询一条数据
    def fetchone(self, sql, params=None):
        '''
        根据sql和参数获取一行数据
        :param sql: sql语句
        :param params: sql语句对象的参数元组，默认值为None
        :return: 查询的一行数据
        '''
        data_one = None

        try:
            count = self.cursor.execute(sql, params)
            if count != 0:
                data_one = self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return data_one

    # 查询多条数据
    def fetchall(self, sql, params=None):
        '''
        根据sql和参数获取一行数据
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 查询的一行数据
        '''

        data_all = None

        try:
            count = self.cursor.execute(sql, params)
            if count != 0:
                data_all = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return data_all

    def __item(self, sql, params=None):
        '''
        执行增删改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        count = 0
        try:
            count = self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
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

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    sql = 'select * from test_user;'
    data = MySqlConnection().fetchall(sql)
    print(data)
