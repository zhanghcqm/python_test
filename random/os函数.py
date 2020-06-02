import os
os.getcwd()
os.getlistdir(path) ##返回指定目录下的所有文件和目录名
os.remove()         ##删除一个文件
os.removedirs(path) ##删除多个目录
os.chdir(path)      ##更改工作区目录
os.mkdir(path)      ##创建一个文件夹
os.rmdir(path)      ##删除一个文件夹
os.rename(oldname,newname) ##重命名

'''os.path库常用操作'''
os.path.isfile(path)    ##检测路径是否为文件
os.path.isdir()         ##检测路径是否文文件夹
os.path.exists()        ##检测路径是否存在
os.path.splitext()      ##分离文件名和扩展名
os.path.split()         ##返回一个路径的目录名和文件名
os.path.dirname()       ##获得路径的路径名
os.path.basename()      ##获得文件名
os.path.getsize()       ##获得文件大小
os.path.join(path,name) ##返回绝对路径
os.walk(path)           ##自顶向下遍历一个目录，返回一个三元组