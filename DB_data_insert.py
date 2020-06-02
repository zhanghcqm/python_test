#coding:utf-8
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "", "test")
print('连接成功')
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL插入语句
for i in range(1,5):
    ID=int(i)
    test_name='zhang'+str(i)
    test_num=int(i)*2
    sql= "INSERT INTO test_table (ID,test_name,test_num)VALUES('%d','%s',%s')"%(ID,test_name,test_num)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
# 关闭数据库连接
db.close()