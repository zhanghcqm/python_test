'''
姓名、年龄、成绩（语文，数学，英语)[每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
s = Student('yourname',20,[69,88,100])
'''
class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_score(self):
        return max(self.score)
s=Student('zhang',18,[52,56,98])
a=s.get_name()
b=s.get_age()
c=s.get_score()
print('%s的年龄是%d，他的成绩的最高分是%d分'%(a,b,c))