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