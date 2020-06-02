#coding:utf-8
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "", "test")
print('连接成功')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL插入语句
for i in range(5,11):
    Id=int(i)
    name='zhang'+str(i)
    passwd='e10adc3949ba59abbe56e057f20f883e'
    sql= "INSERT INTO ecs_users(user_id,user_name,password)VALUES('%d','%s','%s')"%(Id,name,passwd)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库
        db.commit()
        print('插入成功')
    except:
        # Rollback in case there is any error
        db.rollback()
# 关闭数据库连接
db.close()