# python实战（mysql数据库）
# 基本MVC框架搭建
- (1) **建立MVC框架**
    - ① 模型模块（mode）：处理业务的应用程序，model操作数据库，比如插入，更新，删除。每个模型会提供固定类型的数据给控制模块，另一方面，控制模块可以调用模型的不同方法处理数据，并将处理后的结果返回给视图模型
    - ② 控制模块（controller）：可以被看作是一个介于用户，处理（model），显示（view）之间的中间人。它是用户请求的入口，也是应用处理的入口。控制模块接受用户输入，解析，决定哪一个model和view参与处理，因此，它决定了针对用户请求，选择何种view和model。
    - ③ 视图模块（view）：主要用来显示，通过控制模块获取模型模块处理后的数据，并进行格式化的显示。通过控制模块选择view并显示反馈给用户。view模型的选择是基于模型模块的l选择和用户配置等等。
- (2) **配置文件**：setting.py
- (3) **程序入口脚本文件**：user_run.py
- (4) **框架所需要的第三方包**：requirements.txt
## mode层
从存储区获取数据，使用pymysql安装包访问mysql数据库
```
1.pymsql作用：连接数据库,其操作方法如下
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
``` 
实例
```python
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
``` 
## controller层；业务逻辑层
获取用户输入，并将模型与视图建立联系
```python
from mode.base import Mysql

# 定义一个类
class Student():
    def __init__(self):
        # #初始化mysql对象
        self.mysql = Mysql()
    #添加学生的业务
    def add_student(self,*args):
        #固定的sql语句
        # sql= "INSERT INTO students(studentNo,name,age,class,card,city) VALUES(13,'lili','女','4班','234567843267892456','北京')"
        #将可元组*args转化为列表lst：list()
        lst= list(args)
        #若传入的参数列表的长度小于7个值时，将未传入的参数值设置为空字符串
        while len(lst) <=6:
            lst.append('')
        #变化的sql语句：格式化
        sql_form = "INSERT INTO students(studentNo,name,age,class,card,city) " \
                   "VALUES({},'{}','{}','{}','{}','{}')".format(*args)
        result = self.mysql.update(sql_form)
        if not result:
            print("添加学生成功")
        else:
            print("添加学生失败")

    #删除学生的业务

    #修改学生的业务
    def mod_student(self,col_name,value,id):
        sql = "UPDATE students SET {} = '{}' WHERE studentNo = {}".format(col_name,value,id)
        result = self.mysql.update(sql)
        if not result:
            print("修改成功")
        else:
            print("修改不成功")
    #查询学生的业务
    def get_student(self, name):
        sql = "select * from students where name like '%{}%'".format(name)
        print(sql)
        result = self.mysql.get_all(sql)
        if result:
            print("查询结果成功:{}".format(result))
        else:
            print("查询失败")

if __name__ == '__main__':
    s = Student()
    #1.查询学生数据
    # s.get_student('李艾')
    # #2. 插入学生数据
    # s.add_student(16,'李0','女','8班')  #传入参数小于6
    # s.add_student(17, '李1', '女', '7班', '234567843267892456', '北京')  #传入参数等于6
    # s.add_student(18, '李2', '女', '9班', '234567843267892456', '北京','信息学院')  #传入参数大于6
    #3. 修改学生数据
    s.mod_student('age','30',9)
``` 

## view层：用户界面层
展示给用户，从模型获取的数据，使用user_run.py代替
## 其他文件
### requirements.txt
```
# 本框架所需要的所有第三方包，若存在pycharm将会提示安装安装
# 连接数据并固定mysql版本：查看mysql版本：pip show pymysql
pymysql==1.0.2
``` 
### setting.py
```python
#配置文件：配置信息

#1. 连接数据库的配置信息,大写字母：DB_CONFIG（常量）
DB_CONFIG = {
    'host':'localhost',
    'user':'root',
    'password':'root',
    'database':'school',
    'charset':'utf8'
}
``` 
### user_run.py
```python
# 入口脚本文件：user_run.py
from controller.student import Student
#程序的入口方法，仅限于当前文件执行，如果不是user_run.py文件的main方法不运行
if __name__ == '__main__':

    #判断text，
    """
    1. 当用户传入的值是1或者是’新增‘，就给他调用新增，继续传入新增所需要的参数
    2. 当用户传入的值是2或者是’修改‘，调用修改方法，继续传入修改参数
    3. 当用户传入的值是3或者是’删除‘，调用删除方法，继续传入删除参数
    4. 否则，就调用查询方法
    """
    st = Student()
    text = input("请输入数据")
    if text in ['1','新增']:
        print("开始调用新增的方法")
        # 用户输入数据是不能有引号：19 张磊 20 女 2班 24567865432 天津
        add = input()
        # 以空格的方式将字符串add分割并生成列表:lst
        lst = add.split(" ")
        # 将列表lst以可变量参数的方式传入并执行添加学生方法（add_student）
        st.add_student(*lst)
        pass
    elif text in ['2','修改']:
        print("开始调用修改的方法")
        pass
    elif text in ['3','删除']:
        print("开始调用删除的方法")
    else:
        print("开始调用查询方法")
        name = input()
        st.get_student(name)