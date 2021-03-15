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