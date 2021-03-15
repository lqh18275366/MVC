"""
使用pymsql连接数据库且操作方法如下
  （1）导包：import pymysql
  （2）建立连接：pymysql.connect(),并生成对象conn：conn = pymysql.connect()
        connect()需要传入的参数有：
            1)user:代表连接数据库的用户名
            2)password:连接数据的密码
            3)host:连接数据库的主机名
            4)database:连接的数据库名
            5)port：连接端口
            6)charset:设置密码
    (3)建立游标：cursor = conn.cursor()
    (4)执行sql语句：增删改查，例如：cursor。execute(sql)
            查询一条数据：cursor.getone()
            查询所有数据：cursor.getall()
    (5)关闭游标对象：cursor.close()
    (6)关闭连接对象：conn.close()
"""
import pymysql
#导入配置文件
from setting import DB_CONFIG

#定义类
class Mysql():
    # 构造方法
    def __init__(self):
        # 连接数据
        # # 方式1：将连接参数固定
        # self.conn = pymysql.connect(user='root', password='root', host="localhost", database='school', charset='utf8')
        #方式2：将连接数据的参数设置在配置文件（setting）中：user='root',password='root',host="localhost",database='school',charset='utf8'
            # 将配置文件setting中的常量（DB_CONFIG）以字典的形式传入数据库pymysql。connect方法
        self.conn = pymysql.connect(**DB_CONFIG)


    # 增删改的方法
    def update(self,sql):
        print("接收到的sql语句：{}".format(sql))
        try:
            with self.conn.cursor() as cursor:
                # 执行sql语句
                cursor.execute(sql)
                # 将修改的数据提交到数据库
                self.conn.commit()
        # 如果try中的代码块在执行sql时出错时则返回上一步操作不执行改sql语句
        except Exception as e:
            self.conn.rollback()
            return "非空"
        finally:
            if self.conn:
                self.conn.close()
    #查询数据的方法
    def get_all(self,sql):
        try:
            #使用with建立/关闭游标对象 ：cursor
            with self.conn.cursor() as cursor:
                # 执行sql语句
                cursor.execute(sql)
                # 查询sql语句
                result = cursor.fetchall()
                return result
        #try中的代码块若出现异常则处理并打印异常信息
        except Exception as e:
            print(e)
        #以上代码块执行结束后最后断开mysql数据库连接
        finally:
            #如果mysql连接对象存在，则关闭连接对象：conn.close()
            if self.conn:
                self.conn.close()
# 运行base.py文件的入口：main方法
if __name__ == '__main__':
    # 定义一个查询的sql语句并赋值给变量sql
    sql = "select * from students where name = '刘邦'"
    # 定义一个更新的sql语句并赋值给变量update_sql
    update_sql = "update students set class = '7班' where studentNo = 12 "


    # 创建Mysql对象实例
    mysql = Mysql()
    # print(mysql)
    #1. 调用类mydql中的查询方法:get_all并将返回值赋值给result变量
    select_result = mysql.get_all(sql)
    print(select_result)
    # # 2. 调用mysql中的更新方法：update，可通过Navicat查看是否更新成功
    # mysql.update(update_sql)
