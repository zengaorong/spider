#coding=utf-8
import sys
import time
import os
import json
import requests
import math
from sys import getsizeof
reload(sys)
sys.setdefaultencoding('utf-8')
global_data = 0
isbreak = False
def home():
    url_02 = "https://prod-api.ishuhui.com/ver/ea149533/setting/page?page=/&.json"
    ir = requests.get(url_02)
    book_json = json.loads(ir.content)

    # 喵的 改版版结构比原来更加优秀了，这1,2,3，啊什么鬼啊 book_json['data'][1]["data"][1]["data"][1]["viewData"]
    for key in book_json['data'][1]["data"][1]["data"][1]["viewData"]:
        # 章节id 漫画名称 最新章节数 章节名称
        chapater_id =  key['id']
        chapater_book =  key['title']
        chapater_number =  key['minorTitle']
        chapater_title = key['desc']

        url_04 = " https://prod-api.ishuhui.com/comics/detail?id=%s"%chapater_id
        ir = requests.get(url_04)
        decodejson = json.loads(ir.content)
        #这里分两种写法 自己服务器上能用多线程 新浪云上没试验过
        if isbreak:
            break
        load_picture(decodejson["data"]["contentImg"],chapater_book,chapater_title)

def load_picture(url_lists,book_text,title):
    global global_data
    global isbreak
    #url_lists 包括路径和漫画的序号
    picture_dict = url_lists
    load_book_text = book_text
    load_title = title
    #这里在新浪云要变换下
    serchfile = load_book_text + "\\" + load_title
    num = 0
    print "now loading:" + serchfile
    mkdir(load_book_text)
    mkdir(load_book_text + "\\" + load_title)

    time_over = time.strftime('%y-%m',time.localtime(time.time()))
    mkdir(time_over)
    mkdir(time_over + "\\" + serchfile)
    monthfile = time_over + "\\" + serchfile
    bar = ProgressBar(total = len(picture_dict))
    for key in picture_dict:
        #wait_url(time.time())
        #load_url = "http://pic01.ishuhui.com" + picture_dict[key].replace('/upload',"")
        load_url = key["url"]
        #print load_url
        ir = requests.get(load_url,timeout=10)
        global_data = global_data + int(sys.getsizeof(ir.content))
        sz = open(r'%s\%s.jpg'%(serchfile,key["name"]) , 'wb').write(ir.content)
        kz = open(r'%s\%s.jpg'%(monthfile,key["name"]) , 'wb').write(ir.content)
        #print num
        num = num + 1
        bar.move()
        bar.log()
    print load_title + "下载完成"

    if global_data > 1024*1024*12:
        print "data > 12M"
        isbreak = True
def mkdir(path):

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    print path
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        #print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        #print path+' 目录已存在'
        return False
class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        #print s
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()

home()