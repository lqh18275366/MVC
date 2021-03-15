# 1.使用pymsql连接数据库且操作方法如下：
#   （1）导包：import pymysql
#   （2）建立连接：pymysql.connect(),并生成对象conn：conn = pymysql.connect()
#         connect()需要传入的参数有：
#             1)user:代表连接数据库的用户名
#             2)password:连接数据的密码
#             3)host:连接数据库的主机名
#             4)database:连接的数据库名
#             5)port：连接端口
#             6)charset:设置密码
#     (3)建立游标：cursor = conn.cursor()
#     (4)执行sql语句：增删改查，例如：cursor。execute(sql)
#             查询一条数据：cursor.getone()
#             查询所有数据：cursor.getall()
#     (5)关闭游标对象：cursor.close()
#     (6)关闭连接对象：conn.close()
