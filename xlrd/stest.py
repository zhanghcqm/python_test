#！/usr/bin/python3.7
# -*- coding: utf-8 -*-
#@Time   :2020/6/2 16:43
#@Author :zhc

"""
xlrd模块常用方法
"""
import xlrd

#打开excel文件并创建对象存储文件
data=xlrd.open_workbook('F:\py\info.xlsx')
#获取文件中所有工作表的名称
names=data.sheet_names()

#根据工作表名称获取行列内容
table=data.sheet_by_name('Sheet1')

#获取工作表的名称、行数、列数
name=table.name
rowNum=table.nrows
cloNum=table.ncols

#获取单元格的内容
a=table.cell(rowx=1,colx=2)
b=table.cell_value(1,2)


#获取单元格数据类型
#0 empty,1 string,2 number,3 data,4 boolean,5 error
t=table.cell(rowx=1,colx=2).ctype

print(a,b,t)