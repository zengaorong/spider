#coding=utf-8
import sys
import json
reload(sys)
sys.setdefaultcoding="utf-8"

# my_list = ["123","abc","你好"]
# print my_list
#
#
class jsondata:
    name = "123"
    leo_list = ["123","abc","你好"]
    def __init__(self):
        self.htr = "123"
        self.listssdsd = ["123","","你好"]
#
# #json.dump(my_list)
#
kkk = jsondata()
mydict = kkk.__dict__
print  kkk.name
with open('data.json', 'w') as json_file:
    json_file.write(json.dumps(mydict))

# class MyClass:
#     #初始化
#     def __init__(self):
#         self.a=2
#         self.b='bb'
# #创建MyClass对象
# myClass=MyClass()
# #添加数据c
# myClass.c=123
# myClass.a=3
# #对象转化为字典
# myClassDict = myClass.__dict__
# #打印字典
# print (myClassDict)
# #字典转化为json
# myClassJson = json.dumps(myClassDict)
# #打印json数据
# print (myClassJson)

# with open('data.json', 'w') as json_file:
#     json_file.write(json.dumps(MyClass.__dict__))


# -*- coding: UTF-8 -*-
# import json
#
# #自定义类
# class MyClass:
#     #初始化
#     def __init__(self):
#         self.a=2
#         self.b='bb'
#
# ##########################
# #创建MyClass对象
# myClass=MyClass()
# #添加数据c
# myClass.c=123
# myClass.a=3
# #对象转化为字典
# myClassDict = myClass.__dict__
# #打印字典
# print (myClassDict)
# #字典转化为json
# myClassJson = json.dumps(myClassDict)
# #打印json数据
# print (myClassJson)
#
#
# ##########################
# #json转化为字典
# myClassReBuild = json.loads(myClassJson)
# #打印重建的字典
# print (myClassReBuild)
# #新建一个新的MyClass对象
# myClass2=MyClass()
# #将字典转化为对象
# myClass2.__dict__=myClassReBuild;
# #打印重建的对象
# print (myClass2.a)