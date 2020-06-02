import pymysql
# 打开数据库连接
def db_connect(sql):
    db = pymysql.connect("localhost", "root", "", "test")
    print('连接成功')
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    cur.execute(sql)
    data = cur.fetchone()
    db.close()
    print(data)

db_connect("select * from ecs_goods")