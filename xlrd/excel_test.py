#！/usr/bin/python3.7
# -*- coding: utf-8 -*-
#@Time   :2020/6/2 14:57
#@Author :zhc

import xlrd
from xlrd import xldate_as_tuple
import datetime

"""
xlrd单元格的数据类型
数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1;根据表格单元格数据类型在程序加以判断
0 empty,1 string,2 number,3 data,4 boolean,5 error
"""


class ExcelData:
    def __init__(self,filepath,sheetname):
        self.filepath=filepath
        self.sheetname=sheetname

        self.data=xlrd.open_workbook(self.filepath)
        self.table=self.data.sheet_by_name(self.sheetname)

        # 获取第一行作为 key 值
        self.keys = self.table.row_values(0)

        # 获取总行数
        self.rowNum = self.table.nrows

        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于 1")
        else:
            datas = []
            for i in range(1,self.rowNum):
                sheet_data={}
                for j in range(self.colNum):
                    #获取单元格数据类型
                    c_tpye=self.table.cell(i,j).ctype
                    #获取单元格数据
                    c_cell=self.table.cell_value(i,j)
                    if c_tpye == 2 and c_cell % 1==0:#如果是整形
                        c_cell=int(c_cell)
                    elif c_tpye==3:
                        #转换datetime对象
                        date = datetime.datetime(*xldate_as_tuple(c_cell,0))
                        c_cell = date.strftime('%Y/%m/%d')
                    elif c_tpye == 4:
                        c_cell = True if c_cell ==1 else False

                     #循环每个有效的单元格，将字段与值对应存储到字典中，
                     #字典的key就是excel表中每列第一行的字段'''
                    sheet_data[self.keys[j]] = c_cell
                datas.append(sheet_data)

            return datas
if __name__ == "__main__":
    filepath = "F:\py\info.xlsx"
    sheetName = "Sheet1"
    data = ExcelData(filepath, sheetName)
    get_data=data.dict_data()
    print(get_data)